from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField(blank=True, null=True)

class Question(models.Model):
    question = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_title = models.CharField(max_length=255)
    question_options = models.Choices(
        ('Option A', 'Option A'),
        ('Option B', 'Option B'),
        ('Option C', 'Option C'),
        ('Option D', 'Option D')
    )
    answer = models.OneToOneField(question_options, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)