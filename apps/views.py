from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.models import User
from apps.serializers import UserSerializers


class CreateUser(CreateAPIView):
    queryset = User
    serializer_class = UserSerializers

