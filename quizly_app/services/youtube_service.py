import yt_dlp
import os
import tempfile

def download_audio(url):
    """
    Downloads the audio from the given YouTube URL and returns the file path.
    The audio is saved in a temporary directory and the path is returned for further processing.
    """
    temp_dir = tempfile.gettempdir()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(temp_dir, "audio.%(ext)s"),
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    file_path = ydl.prepare_filename(info)
    return file_path