from django.db import models
from django.db.models.base import Model
from django.db.models.query_utils import PathInfo

# Create your models here.




class Addresses(models.Model):
  name = models.CharField(max_length=10)
  phone_number = models.CharField(max_length=13)
  address = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created'] # orderby랑 비슷하다고 생각하면 됨. -하면 반대 차순으로 정렬
