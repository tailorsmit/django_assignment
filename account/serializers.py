from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ('id', 'username', 'email')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'mobile_no', 'verified')
        extra_kwargs = {
            'password': {'write_only': True},
            'verified': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['mobile_no'],
                                        validated_data['email'])
        return user
