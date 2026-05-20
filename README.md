# Youtube ID Extract
A simple FastAPI script for Modal that extracts the YouTube ID from any YouTube video URL, regardless of the URL format.

This solution uses a robust regular expression designed to cleanly extract the 11-character video ID from standard watch links, shortened ```youtu.be``` links (with or without tracking query parameters like ```?si=...```), embeds, and YouTube Shorts.

You can call the script like this via curl:
```
curl "https://<your-modal-url>/extract?url=https://youtu.be/<video_id>?si=ZLKZ0dJyw0Fq6w_R"
```
Expect the output for a similar input to be
```json
{
  "success": true,
  "input_url": "https://youtu.be/<video_id??si=ZLKZ0dJyw0Fq6w_R",
  "video_id": "<video_id>",
  "thumbnail_url": "https://img.youtube.com/vi/<video_id>/maxresdefault.jpg"
}
```