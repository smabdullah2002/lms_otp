
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8001/otp/send/
    path('otp/', include('otp.urls')),
]
