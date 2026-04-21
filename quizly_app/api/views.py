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

        # url = self.request.data.get("url")

        # quiz = serializer.save(
        #     video_url=url,
        #     title="processing...",
        #     description="processing..."
        # )

        # process_audio_task.delay(quiz.id, url)



        # url = normalize_youtube_url(url)

        # ydl_opts = {
        #     "format": "bestaudio/best",
        #     "outtmpl": "media/audio/%(id)s.%(ext)s",
        #     "quiet": True,
        #     "noplaylist": True,
        #     "postprocessors": [{
        #         "key": "FFmpegExtractAudio",
        #         "preferredcodec": "mp3",
        #         "preferredquality": "192",
        #     }],
        # }


        # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #     info = ydl.extract_info(url, download=True)
        #     file_path = ydl.prepare_filename(info).replace(".webm", ".mp3")

        # with open(file_path, "rb") as f:
        #     serializer.save(
        #         title=info.get("title"),
        #         description=info.get("description"),
        #         video_url=url,
        #         audio_file=File(f, name=os.path.basename(file_path))
        #     )
        # model = whisper.load_model("turbo")
        # result = model.transcribe(file_path)
        # print(result["text"])