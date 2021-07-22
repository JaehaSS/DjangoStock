from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path('api/tutorials/', views.tutorial_list),
    # path('tuotorals/d', views.tutorial_detail),
    # path('/tutorials/published', views.tutorial_list_published),
    # url(r'^api/tutorials$', views.tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published),
    path('', views.index),
    path('api/', views.bbs_list),
    path('hello/', views.helloAPI),
    path('1/', views.randomQuiz),

]
