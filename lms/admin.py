from django.contrib import admin

from lms.models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'preview', 'description', 'owner',)
    list_filter = ('name', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'preview', 'description', 'video_url',
                    'course', 'owner',)
    list_filter = ('name', 'course', 'owner',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'course', 'status',)
    list_filter = ('owner', 'course', 'status',)
