from rest_framework import serializers

from lms.models import Lesson
from lms.validators import VideoValidators


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'preview', 'owner',
                  'description', 'video_url', 'course']
        validators = [
            VideoValidators(field='video_url'),
            serializers.UniqueTogetherValidator(
                queryset=Lesson.objects.all(),
                fields=['name', 'owner'],
                message='Имя урока должно быть уникальным'
            )
        ]
