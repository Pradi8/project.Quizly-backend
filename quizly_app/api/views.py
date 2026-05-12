from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_app.api.permissions import IsQuizlyUser
from quizly_app.api.serializers import QuizSerializer
from quizly_app.models import Quiz
from quizly_app.tasks import process_video

from quizly_app.standardurl import normalize_youtube_url

class QuizListView(generics.ListCreateAPIView):
    """
    API view for listing all quizzes and creating a new quiz.
    - GET: Returns a list of all quizzes.
    - POST: Creates a new quiz, normalizes the YouTube URL,
      saves the quiz with the authenticated user,
      and synchronously processes the video to generate quiz content.
    """
        
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        url = request.data.get("url")
        normalized_url = normalize_youtube_url(url)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quiz = serializer.save(video_url=normalized_url, user=request.user)

        # Process the video synchronously to generate quiz content
        process_video(quiz.id, quiz.video_url)

        # Reload the quiz from the database because
        # new questions and metadata may have been added
        quiz.refresh_from_db()

        return Response(
            QuizSerializer(quiz).data,
            status=status.HTTP_201_CREATED
        )
    
class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single quiz.

    - GET: Retrieve quiz details
    - PATCH/PUT: Update quiz fields
    - DELETE: Delete the quiz

    Access is restricted to the quiz owner via custom permission.
    """
        
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsQuizlyUser]