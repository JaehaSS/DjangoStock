from django.urls import path
from user.api.views import CurrentUserAPIView, UserlistAPIView


urlpatterns = [
path("user/", CurrentUserAPIView.as_view(), name="current-user"),
path("userlist/", UserlistAPIView.as_view(), name= "Userlist" )
]
