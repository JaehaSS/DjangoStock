from django.db import models
from rest_framework import serializers
from user.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]



class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
