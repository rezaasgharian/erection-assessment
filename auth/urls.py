from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from auth.views import RegisterAPIView

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),

]