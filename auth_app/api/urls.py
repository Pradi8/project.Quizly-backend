from django.urls import path
from .views import RegistrationView

# ------------------------------
# Endpoints
# ------------------------------

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
]