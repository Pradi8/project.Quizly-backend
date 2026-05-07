import whisper

model = whisper.load_model("small")

def transcribe_audio(file_path):
    result = model.transcribe(file_path, fp16=False)
    return result["text"]

