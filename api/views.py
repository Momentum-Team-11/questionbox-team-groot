from core.models import User, Question, Response
from .serializers import UserSerializer, QuestionSerializer, ResponseSerializer, QuestionResponseSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResponseListView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class QuestionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionResponseSerializer

class QuestionResponseView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = QuestionResponseSerializer