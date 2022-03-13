from rest_framework import generics
from django.contrib.auth.models import User
# from .serializers import AuthTokenObtainPairSerializer, RegisterSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView


# class ObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = AuthTokenObtainPairSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

