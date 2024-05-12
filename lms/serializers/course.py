"""
Сериализатор для класса Курс
"""

from rest_framework import serializers

from lms.models import Course, Subscription
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для курса.
    """

    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description',
                  'lesson_count', 'lesson', 'subscription']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Course.objects.all(),
                fields=['name',],
                message='Имя курса должно быть уникальным'
            )
        ]

    def get_lesson_count(self, instance):
        return instance.lessons.count()

    def get_subscription(self, instance):
        subscription = Subscription.objects.filter(
            course=instance,
            owner=self.context.get('request').user
        ).all()
        if subscription:
            return True
        else:
            return False
