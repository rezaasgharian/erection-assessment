from django.urls import path
from .views import UserQuestionnairesViewAPI, QuestionnaireListCreateAPI

urlpatterns = [
    path('questionnaire/', UserQuestionnairesViewAPI.as_view(), name='questionnaires'),
    path('create/', QuestionnaireListCreateAPI.as_view(), name='create'),
]
