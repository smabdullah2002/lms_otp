from django.db import models
from ._applib.models_choice_field import Status

class OtpModel(models.Model):
    otp_for= models.CharField(max_length=100)
    identifier= models.CharField(max_length=100)
    reason= models.CharField(max_length=100)
    otp= models.CharField(max_length=10)
    status=models.CharField(max_length=20,choices=Status.choices, default=Status.INITIALIZE)
    message=models.TextField(null=True, blank=True)
    expires_at=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    verified_at=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.otp_for + " - " + self.identifier
    
    
    class Meta:
        verbose_name= "OTP Model"
        verbose_name_plural= "OTP Models"
        db_table= "otp_model"