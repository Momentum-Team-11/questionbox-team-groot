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
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    photo = serializers.SlugRelatedField(slug_field='photo', read_only='True'),
    class Meta:
        model = Question
        fields = (
            "pk",
            "user_first_name",
            "user_last_name",
            "username",
            "photo",
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
    responses = ResponseSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "responses",
        )