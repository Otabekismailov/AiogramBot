from rest_framework import serializers

from apps.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'firs_name', 'user_id')
