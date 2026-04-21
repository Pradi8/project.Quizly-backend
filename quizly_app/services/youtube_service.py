import yt_dlp

def download_audio(url, quiz_id):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"media/audio/{quiz_id}.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        file_path = ydl.prepare_filename(info).replace(".webm", ".mp3")

    return file_path, info