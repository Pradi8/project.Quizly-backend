from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from quizly_app.api.serializers import QuizSerializer
from quizly_app.models import Quiz
from quizly_app.tasks import process_video

from quizly_app.standardurl import normalize_youtube_url

class QuizListView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        url = request.data.get("url")
        normalized_url = normalize_youtube_url(url)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quiz = serializer.save(video_url=normalized_url)

        # 🔥 SYNCHRON (blockiert!)
        process_video(quiz.id, quiz.video_url)

        # 🔄 neu laden, weil Questions erstellt wurden
        quiz.refresh_from_db()

        return Response(
            QuizSerializer(quiz).data,
            status=status.HTTP_201_CREATED
        )