from rest_framework import viewsets

from lms.models import Course
from lms.paginations.course import CoursePagination
from lms.serializers.course import CourseSerializer
from lms.tasks import send_email_for_update_course
from users.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePagination

    def get_permissions(self):
        """
        Определяем права доступа по запрашиваемому действию
        :return: Уровень доступа
        """
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """
        Привязать пользователя к созданному курсу
        """
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        """
        Отправить сообщение об изменении курса всем подписанным абонентам
        :param serializer:
        :return:
        """
        course = serializer.save()
        course_id = course.id
        send_email_for_update_course.delay(course_id)
