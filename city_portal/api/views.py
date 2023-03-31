from rest_framework import generics
from rest_framework.decorators import action
from django.http import HttpResponseNotFound
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render

from .models import *
from .serializers import *
from .permissions import *


def base(request):
    return render(request, 'api/base.html')

class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ApiAPIList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class ApiAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    permission_classes = (IsAuthenticated, )


class ApiAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    permission_classes = (IsAdminOrReadOnly, )

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
