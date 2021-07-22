from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.urls import path,include
from .Api import HtmlTest, JsonTest


urlpatterns = [
    # path('json/', JsonTest.all_users, name='JsonAllUser'),
    # path('json/<username>', JsonTest.specific_user, name='JsonSpecificUser'),
    # path('html/', HtmlTest.all_users, name='HtmlAllUser'),
    # path('html/<username>', HtmlTest.specific_user, name='HtmlSpecificUser'),
    path('', views.index,name="index"),

]