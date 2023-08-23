from rest_framework.generics import ListCreateAPIView, ListAPIView
from apps.models import User, Category, Commit, DjangoCourse
from rest_framework import generics

from rest_framework.views import APIView
from apps.serializers import UserSerializers, CategorySerializers, CategoryParentSerializers, CommitSerializers, \
    CourseSerializers


class CreateUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class CategoryListApi(ListAPIView):
    queryset = Category.objects.filter(parent_id=None)
    serializer_class = CategorySerializers


class CategoryParent(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryParentSerializers

    def get_queryset(self):
        qs = self.queryset.filter(parent_id=self.kwargs.get("pk"))
        if qs:
            return qs
        else:
            return None


class CommitCreateList(ListCreateAPIView):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializers


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializers

    def get_queryset(self):
        qs = DjangoCourse.objects.filter(category_id=self.kwargs.get("pk"))
        if qs:
            return qs
        return None
