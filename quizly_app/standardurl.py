from urllib.parse import urlparse, parse_qs

def normalize_youtube_url(url: str) -> str | None:
    """
    Normalize different YouTube URL formats into a standard format.
    This function extracts the video ID from a given YouTube URL
    (e.g. short links like youtu.be or standard watch URLs) and
    returns a consistent URL in the form:

        https://www.youtube.com/watch?v=VIDEO_ID

    If the input URL is not a valid or supported YouTube URL,
    the function returns None.
    """
    # Parse the URL into its components:
    # - scheme: protocol (e.g. "http", "https")
    # - netloc: domain name (e.g. "www.youtube.com", "youtu.be")
    # - path: the path after the domain (e.g. "/watch", "/VIDEO_ID")
    # - query: URL parameters (e.g. "v=VIDEO_ID&si=abc")
    parsed = urlparse(url)

    # Case 1: Short YouTube URL (youtu.be)# Fall 1: youtu.be/VIDEO_ID
    if parsed.netloc == "youtu.be":
        video_id = parsed.path.strip("/")

    # Case 2: Standard YouTube watch URL (youtube.com/watch?v=...)
    elif "youtube.com" in parsed.netloc:
        query = parse_qs(parsed.query)
        video_id = query.get("v", [None])[0]
    else:
        return None
    if not video_id:
        return None
    return f"https://www.youtube.com/watch?v={video_id}"