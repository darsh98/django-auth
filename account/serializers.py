from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            user.deviceId=data.get('deviceId',None)
            data = {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
                }
            return data
        raise serializers.ValidationError('Email or Password is wrong.')


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'password']
        read_only_fields = ['id']
        write_only_fields = ['password']
        require = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

