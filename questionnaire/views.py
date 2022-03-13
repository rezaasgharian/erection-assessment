from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Questionnaire
from .serializers import QuestionnaireSerializer


class QuestionnaireListCreateAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Questionnaire.objects.filter(user_id=self.request.user)
        else:
            return Questionnaire.objects.none()


class UserQuestionnairesViewAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionnaireSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        user = self.request.user.id
        queryset = self.model.objects.filter(user=user)
        return queryset.order_by('-created_at')


class QuestionnaireViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
