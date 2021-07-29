from django.db.models import fields
from rest_framework import serializers
from .models import Addresses
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = User
    fields = ('username', 'password')


class AddressesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Addresses
    fields = ['name', 'phone_number', 'address']


