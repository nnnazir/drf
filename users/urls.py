from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserUpdateAPIView,
                         UserDestroyAPIView, UserRetrieveAPIView,
                         UserListAPIView, MyTokenObtainPairView)


app_name = UsersConfig.name

# Описание маршрутизации для ViewSet
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/delete/<int:pk>/', UserDestroyAPIView.as_view(),
         name='user_delete'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(),
         name='user_update'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('users/list/', UserListAPIView.as_view(), name='user_list'),
]
