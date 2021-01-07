from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserViews.as_view(), name='me'),
    path('request-otp/', views.request_otp, name='req_otp'),
    path('verify-otp/<int:otp>', views.verifyotp, name='verify')
]
