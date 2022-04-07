from core.models import User, Question, Response
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "photo",
            "about",
        )

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "pk",
            "user",
            "title",
            "question",
            "date_asked",
        )

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = (
            "pk",
            "user",
            "question",
            "answer",
            "date_answered",
        )

class QuestionResponseSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True, required=False, source='responses')
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "responses",
        )