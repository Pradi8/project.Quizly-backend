from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from quizly_app.api.serializers import QuizSerializer
from quizly_app.models import Quiz
from google import genai
import json
import yt_dlp
import whisper

from quizly_app.standardurl import normalize_youtube_url

class QuizListView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        url = self.request.data.get("url")
        url = normalize_youtube_url(url)
        with yt_dlp.YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        serializer.save(
            title=info.get("title"),
            description=info.get("description"),
            video_url=url
        )