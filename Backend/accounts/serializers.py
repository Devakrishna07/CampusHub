from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'authorized_events']

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'authorized_events']

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data.get('email'),
                password=validated_data['password'],
                role=validated_data['role'],
            )
            user.set_password(validated_data['password'])
            user.save()
            user.authorized_events.set(validated_data.get('authorized_events', []))
            return user