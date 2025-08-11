from django.shortcuts import render
from rest_framework.views import APIView
from requests import request
from .models import OtpModel
from datetime import datetime, timedelta
from rest_framework.response import Response
from ._applib.otp_generator import generator


class OtpSenderView(APIView):
    def post(self,request):
        data= request.data
        current_time=datetime.now()
        duration= timedelta(minutes=2)
        generated_otp= generator()
        OtpModel.objects.create(
            otp_for= data.get("otp_for"),
            identifier= data.get("identifier"),
            reason= data.get("reason"),
            otp= generated_otp,
            message= data.get("message"),
            expires_at= current_time + duration,
        )
    
        return Response(
            {"message": "OTP sent successfully."},
        )
