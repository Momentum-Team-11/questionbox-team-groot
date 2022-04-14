from core.models import User, Question, Response
from .serializers import UserSerializer, QuestionSerializer, ResponseSerializer, QuestionResponseSerializer
from rest_framework import generics
from rest_framework.decorators import action

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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuestionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionResponseSerializer

    def get_queryset(self):
        return self.order_by('pk')

class ResponseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def accepted(self, request):
        accepted_answers = Question.objects.filter(accepted=True)
        serializer = self.get_serializer(accepted_answers, many=True)
        return Response(serializer.data)

class QuestionResponseView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def get_queryset(self):
        return self.request.user.user_responses.order_by('pk')

class UserQuestionsView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return self.request.user.questions.all()

class UserResponsesView(generics.ListAPIView):
    serializer_class = ResponseSerializer
    def get_queryset(self):
        return self.request.user.user_responses.all()

class QuestionSearchView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        search_term = self.request.query_params.get("question")
        if search_term is not None:
            return Question.objects.filter(question__icontains=search_term)

class QuestionFavoriteView(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    @action(detail=False, methods=['get'])
    def favorited(self, request):
        question = self.get_queryset().filter(favorited=True).filter(user_id=self.request.user)
        serializer = self.get_serializer(question, many=True)
        return Response(serializer.data)

class AnswerFavoriteView(generics.RetrieveUpdateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    @action(detail=False, methods=['get'])
    def favorited(self, request):
        response = self.get_queryset().filter(favorited=True).filter(user_id=self.request.user)
        serializer = self.get_serializer(response, many=True)
        return Response(serializer.data)