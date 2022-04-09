from core.models import User, Question, Response
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    class Meta:
        model = User
        fields = (
            "id",
            "user_first_name",
            "user_last_name",
            "username",
            "photo",
            "about",
        )

class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    class Meta:
        model = Question
        fields = (
            "pk",
            "user_first_name",
            "user_last_name",
            "username",
            "title",
            "question",
            "date_asked",
        )

class ResponseSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username
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
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "question",
            "date_asked",
            "user",
            "responses",
        )

# class UserQuestionsSerializer(serializers.ModelSerializer):

# class UserProfileSerializer(serializers.ModelSerializer):