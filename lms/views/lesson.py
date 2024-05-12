"""
Вьюшки Generic-классы для класса Уроки
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from lms.models import Lesson
from lms.paginations.lesson import LessonPagination
from lms.permissions import IsOwnerOrStaff
from lms.serializers.lesson import LessonSerializer
from users.permissions import IsOwner, IsModerator


class LessonListView(generics.ListAPIView):
    """
    Вьюшка для списка уроков
    """
    permission_classes = [IsAuthenticated,]
    pagination_class = LessonPagination
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_fields = ('name', 'description', 'course', 'owner')
    filterset_fields = ('name', 'description', 'course', 'owner')
    search_fields = ('^name', )
    ordering_fields = ('name',)

    def get(self, request):
        pagination_queryset = self.paginate_queryset(self.queryset)
        serializer_class = LessonSerializer(pagination_queryset, many=True)
        return self.get_paginated_response(serializer_class.data)

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """
        Привязать пользователя к созданному уроку
        """
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]
