from rest_framework.generics import ListCreateAPIView
from apps.models import User
from apps.serializers import UserSerializers


class CreateUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
