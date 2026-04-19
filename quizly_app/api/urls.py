from django.urls import path

from quizly_app.api.views import QuizListView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz-list-view'),
    # path('questions/', include('quizly_app.api.question_urls')),
]