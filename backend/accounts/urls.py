from django.urls import path
from .views import*

urlpatterns = [
    path('linkedin/', LinkedInSocialAuthView.as_view()),
]
