from django.urls import path
from .views import *

urlpatterns = [
    path('', regist),
    path('home/', home, name='home'),
    path('login/', login, name="login"),

]
