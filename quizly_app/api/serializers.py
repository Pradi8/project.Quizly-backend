from rest_framework import serializers
from quizly_app.models import Question, Quiz

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options', 'answer', 'created_at', 'updated_at']
        
class QuizSerializer(serializers.ModelSerializer):

    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    # Request-Field
    url = serializers.URLField(write_only=True)

    # Response-Field
    video_url = serializers.URLField(read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'video_url', 'url']

    def create(self, validated_data):
        validated_data.pop("url")
        return super().create(validated_data)
    