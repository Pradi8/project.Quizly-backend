import yt_dlp
import os
import tempfile

def download_audio(url):
    temp_dir = tempfile.gettempdir()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(temp_dir, "audio.%(ext)s"),
        # "postprocessors": [
        #     {
        #         "key": "FFmpegExtractAudio",
        #         "preferredcodec": "mp3",
        #         "preferredquality": "192",
        #     }
        # ],
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    file_path = ydl.prepare_filename(info)
    return file_path
