from rest_framework import serializers
from quizly_app.models import Question, Quiz

class QuestionSerializer(serializers.ModelSerializer):
    """ 
    Serializer for Question model. 
    """
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options', 'answer', 'created_at', 'updated_at']
        
class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer for Quiz model.
    """

    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    # Request-Field
    url = serializers.URLField(write_only=True)

    # Response-Field
    video_url = serializers.URLField(read_only=True)

    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'video_url', 'url', 'questions']

    def create(self, validated_data):
        validated_data.pop("url")
        return super().create(validated_data)
    