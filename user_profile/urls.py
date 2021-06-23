from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.user_profile, name = 'user_profile'),
]