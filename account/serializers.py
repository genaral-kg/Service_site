from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Spam_Contacts, CustomUser

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    user = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'last_name', 'first_name','avatar', 'user')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Пароли не совпадают!')
        if attrs['password'].isalpha():
            raise serializers.ValidationError(
                'Пароль должен содержать в себе буквы и цифры. Минимальная длина - 8 знаков.')
        if attrs['password'].isdigit():
            raise serializers.ValidationError(
                'Пароль должен содержать в себе буквы и цифры. Минимальная длина - 8 знаков.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {'bad_token': _('Token is invalid or expired!')}

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ForgotPasswordSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)


class RestorePasswordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(min_length=8, required=True)
    password2 = serializers.CharField(min_length=8, required=True)

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Passwords didn\'t match!')
        try:
            user = User.objects.get(
                activation_code=attrs['code']
            )
        except User.DoesNotExist:
            raise serializers.ValidationError('Your code is incorrect!')
        attrs['user'] = user
        return attrs

    def save(self, **kwargs):
        data = self.validated_data
        user = data['user']
        user.set_password(data['password'])
        user.activation_code = ''
        user.save()
        return user

# ----------SPAM -----------MESSAGE----------#
class SpamViewSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = Spam_Contacts
        fields = "__all__"

    def validate(self,attrs):
        email = self.context['request'].user.email
        if Spam_Contacts.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'You are already followed to spam!'
            )
        return attrs


class ExecuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        exclude = ('password','id','is_superuser','is_staff','activation_code','user_permissions','groups',)




