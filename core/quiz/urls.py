"""
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
"""
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('q/', Question.as_view(), name='question'),
    path('a/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='RandomQuestionTopic'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)