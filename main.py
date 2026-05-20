import re
import modal
from fastapi import FastAPI, HTTPException, Query

# Initialize FastAPI app
web_app = FastAPI(
    title="YouTube ID Extractor", 
    description="A simple API to parse video IDs from various YouTube URL formats."
)

# Initialize Modal App (Note: 'Stub' was renamed to 'App' in newer Modal versions)
app = modal.App("youtube-id-extractor")

# Regex to capture the 11-character YouTube video ID across different URL structures
YOUTUBE_REGEX = re.compile(
    r'(?:v=|\/v\/|\/embed\/|\/shorts\/|\.be\/)([a-zA-Z0-9_-]{11})'
)

@web_app.get("/extract")
def extract_id(url: str = Query(..., description="The YouTube URL to parse")):
    """
    Extracts the video ID from a provided YouTube URL.
    Supports standard, shortened, tracking-heavy, embed, and shorts formats.
    """
    match = YOUTUBE_REGEX.search(url)
    
    if not match:
        raise HTTPException(
            status_code=400, 
            detail="Could not extract a valid 11-character YouTube video ID from the provided URL."
        )
        
    video_id = match.group(1)
    return {
        "success": True,
        "input_url": url,
        "video_id": video_id,
        "thumbnail_url": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    }

@app.function(image=modal.Image.debian_slim())
@modal.asgi_app()
def fastapi_app():
    return web_app