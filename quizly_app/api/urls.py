from django.urls import path
from quizly_app.api.views import QuizDetailView, QuizListView

# ------------------------------
# Endpoints Quizly:
# ------------------------------

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz-list-view'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail-view'),
]