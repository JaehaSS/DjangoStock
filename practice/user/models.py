from django.db import models #Django default setting
from django.contrib.auth.models import AbstractUser #장고에서 제공하는 사용자 모델을 그대로 가져와 사용하자.


class CustomUser(AbstractUser):
  def __str__(self):
    return self.username
