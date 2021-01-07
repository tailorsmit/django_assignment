from rest_framework import generics, authentication, permissions, response
from user.serializers import UserSerializer, AuthTokenSerializer
from .models import Otp
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
import random


class CreateUserView(generics.CreateAPIView):
    """create a new user"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """create new Token"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserViews(generics.RetrieveUpdateAPIView):
    """manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """retrive and return authentication user"""
        return self.request.user


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def request_otp(request):
    if request.user.verified:
        return response.Response({'message': 'user already verified'})
    usr_otp = str(random.randint(100000, 999999))
    # Another approach for otp
    # temp = ""
    # for _ in range(6):
    #     temp += str(random.randint(0, 9))
    #  send_otp_via_sms(usr_otp)
    print(usr_otp)
    user = Otp.objects.filter(user=request.user)
    if not user:
        Otp.objects.create(user=request.user, otp=usr_otp)
    else:
        Otp.objects.filter(user=request.user).update(otp=usr_otp)
    return response.Response({'message': 'otp sent successfully'})


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def verifyotp(request, otp):
    if request.user.verified:
        return response.Response({'message': 'user already verified'})
    get_otp = str(otp)
    user_otp = str(Otp.objects.filter(user=request.user).last())
    print(user_otp)
    if user_otp == get_otp:
        x = request.user
        x.verified = True
        x.save()
        return response.Response({'message': 'phone number verified'})
    return response.Response({'message': 'otp invalid'})
