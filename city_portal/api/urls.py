from django.urls import path
from .views import *

urlpatterns = [
    path('', base),
    path('', RegisterUser.as_view()),
]
