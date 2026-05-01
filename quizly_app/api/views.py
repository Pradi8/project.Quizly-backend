from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from quizly_app.api.serializers import QuizSerializer
from quizly_app.models import Quiz
from quizly_app.tasks import process_video
import django_rq

from quizly_app.standardurl import normalize_youtube_url

class QuizListView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        url = self.request.data.get("url")
        quiz = serializer.save(video_url=url, status="processing")

        # 🔥 Task in Queue
        django_rq.enqueue(process_video, quiz.id, quiz.video_url)