from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Subscription
from lms.serializers.subscription import SubscriptionSerializer
from users.permissions import IsOwner


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, *args, **kwargs):

        course = Course.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        subscription = Subscription.objects.filter(course=course,
                                                   owner=user).first()

        if subscription.status:
            subscription.status = False
            subscription.save()
            message = 'Вы отписались от курса.'
        else:
            subscription.status = True
            subscription.save()
            message = 'Вы подписались на курс.'

        return Response({"message": message})
