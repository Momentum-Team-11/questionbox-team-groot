from django.contrib import admin
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/questions', api_views.QuestionListView.as_view(), name='api_questions_list'),
    path('api/question/<int:pk>', api_views.QuestionDetailsView.as_view(), name='api_question_details'),
    path('api/question/response/<int:pk>/', api_views.ResponseDetailView.as_view(), name='response-detail'),
    path('api/responses', api_views.ResponseListView.as_view(), name='api_responses_list'),
    path('api/users', api_views.UserListView.as_view(), name='user_list'),
    path('api/question/<int:pk>/response', api_views.QuestionResponseView.as_view(), name='api_question_response'),
    path('api/users/<int:pk>/', api_views.UserQuestionsView.as_view(), name='user-detail'),
    path('api/myquestions/', api_views.UserQuestionsView.as_view(), name='my-questions'),
    path('api/myresponses', api_views.UserResponsesView.as_view(), name='my-responses'),
    path('api/search', api_views.QuestionSearchView.as_view(), name='question-search'),
    path('api/questions/favorite/<int:pk>', api_views.QuestionFavoriteView.as_view(), name='favorited'),
]