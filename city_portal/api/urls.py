from django.urls import path
from .views import *

urlpatterns = [
    path('', regist, name="regist"),
    path('home/', home, name='home'),
    path('login/', login, name="login"),
    path('logout/', logout_user, name='logout'),
]
