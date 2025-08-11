from django.urls import path
from .views import OtpSenderView

urlpatterns=[
    path('send/', OtpSenderView.as_view(), name='send_otp'),
]