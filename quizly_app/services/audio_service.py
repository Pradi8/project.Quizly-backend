import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("small")

    """
    Transcribes the audio file at the given path using the Whisper model.
    """

    result = model.transcribe(file_path, fp16=False)
    return result["text"]