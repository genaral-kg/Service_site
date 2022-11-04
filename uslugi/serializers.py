from django.contrib.auth import get_user_model
from rest_framework import serializers

from uslugi.models import Uslugi

User = get_user_model()


class UslugiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Uslugi
        fields = "__all__"

    def validate(self,attrs):
        a = self._context['request']
        if a.user.user != 2:
            raise serializers.ValidationError(
                'You are not executor!'
            )
        return attrs
