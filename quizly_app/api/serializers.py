from rest_framework import serializers
from quizly_app.models import Question, Quiz
from quizly_app.standardurl import normalize_youtube_url
from google import genai
import json
import yt_dlp
import whisper

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'answer', 'created_at', 'updated_at']
        
class QuizSerializer(serializers.ModelSerializer):

    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    # Request-Field
    url = serializers.URLField(write_only=True)

    # Response-Field
    video_url = serializers.URLField(read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'video_url', 'url']

    def create(self, validated_data):
        validated_data.pop("url")
        return super().create(validated_data)
    

# yt-dlp

# URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'

# # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
# ydl_opts = {
#     "format": "bestaudio/best",

#     "outtmpl": tmp_filename,

#     "quiet": True,

#     "noplaylist": True,
# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=False)

#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     print(json.dumps(ydl.sanitize_info(info)))


# #whisper

# model = whisper.load_model("turbo")
# result = model.transcribe("audio.mp3")
# print(result["text"])

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents=Question.objects.first().question_title
# )
# print(response.text)
