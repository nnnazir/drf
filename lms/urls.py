from django.urls import path

from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.lesson import (LessonListView, LessonCreateView,
                              LessonDetailView, LessonUpdateView,
                              LessonDestroyView)
from lms.views.subscription import SubscriptionAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(),
         name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(),
         name='lesson_delete'),
    path('courses/<int:pk>/subscription/', SubscriptionAPIView.as_view(),
         name='subscription')
] + router.urls
