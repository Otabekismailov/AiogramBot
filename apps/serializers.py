from rest_framework import serializers

from apps.models import User, DjangoCourse, Commit, Category, CourseVideo


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'first_name', 'chat_id')


class CourseVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ("id", "video",)


class CourseSerializers(serializers.ModelSerializer):
    course_video = serializers.SerializerMethodField()

    def get_course_video(self, obj):
        return obj.course_video.values('video')

    class Meta:
        model = DjangoCourse
        fields = ("id", "title", "course_video")


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class CategoryParentSerializers(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ("id", "name",)


class CommitSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Commit
        fields = ("id", "description", "user")
