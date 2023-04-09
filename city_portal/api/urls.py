from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterUser.as_view(), name="regist"),
    path('profile/', profile, name='profile'),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name='logout'),
    path('application/', application, name="application"),
]
