from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'mobile_no', 'verified',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5},
                        'mobile_no': {'min_length': 10},
                        'verified': {'read_only': True}}

    def create(self, validated_data):
        """create a new user with encrypted pass word"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """update a user , setting the password"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """serializer for authentication"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate users"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _("unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
