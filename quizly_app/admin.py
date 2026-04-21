from django.contrib import admin
from .models import Quiz, Question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status")
    list_filter = ("status",)

admin.site.register(Question)