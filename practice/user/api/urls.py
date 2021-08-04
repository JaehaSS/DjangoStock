from django.urls import path
from user.api.views import CurrentUserAPIView, UserlistAPIView
from user.api.views import parse_blog

urlpatterns = [
path("user/", CurrentUserAPIView.as_view(), name="current-user"),
path("userlist/", UserlistAPIView.as_view(), name= "Userlist" ),
path("stockdata/", parse_blog, name= "parse_blog" ),
]
