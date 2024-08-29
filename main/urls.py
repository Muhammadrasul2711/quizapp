from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz-list', views.quizList, name='quizList'),
    path('quiz-detail/<int:id>/', views.quizDetail, name='quizDetail'),
    path('create-quiz', views.createQuiz, name='createQuiz'),
    path('create-question/<int:id>/', views.questionCreate, name='questionCreate'),
    path('question-detail/<int:id>/', views.questionDetail, name='questionDetail'),
    path('option-create/<int:id>/', views.optionCreate, name='optionCreate'),
    path('option-delete/<int:id>/', views.optionDelete, name='optionDelete')
]