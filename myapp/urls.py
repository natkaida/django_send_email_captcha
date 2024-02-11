from django.urls import path
from .views import ApplicationView, SuccessView, refresh_captcha

urlpatterns = [
    path('application/', ApplicationView.as_view(), name='application'),
    path('success/', SuccessView.as_view(), name='success'),
    path('captcha/refresh/', refresh_captcha, name='refresh_captcha'),
]


