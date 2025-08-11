from django.contrib import admin
from .models import OtpModel

@admin.register(OtpModel)
class OtpModelAdmin(admin.ModelAdmin):
    list_display=(
        'identifier',
        'otp_for',
        'reason',
        'otp',
        'status',
        'expires_at',
        'created_at',
        'updated_at',
    )

