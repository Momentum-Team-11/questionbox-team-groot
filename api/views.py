from core.models import User, Question, Response
from .serializers import UserSerializer, QuestionSerializer, ResponseSerializer, QuestionResponseSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResponseListView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class QuestionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionResponseSerializer

    def accepted(self, request):
        accepted_answers = Question.objects.filter(accepted=True)
        serializer = self.get_serializer(accepted_answers, many=True)
        return Response(serializer.data)

class QuestionResponseView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class UserQuestionsView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return self.request.user.questions.all()

class UserResponsesView(generics.ListAPIView):
    serializer_class = QuestionResponseSerializer
    def get_queryset(self):
        return self.request.user.user_responses.all()

class QuestionSearchView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        search_term = self.request.query_params.get("question")
        if search_term is not None:
            return Question.objects.filter(question__icontains=search_term)