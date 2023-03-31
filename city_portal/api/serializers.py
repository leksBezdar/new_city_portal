from rest_framework import serializers

from .models import *


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
