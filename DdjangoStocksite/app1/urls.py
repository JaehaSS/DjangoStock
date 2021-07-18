from django.conf.urls import url 
from . import views 
from django.urls import path
 
urlpatterns = [ 
    path('tutorials/', views.tutorial_list),
    path('tuotorals/d', views.tutorial_detail),
    path('/tutorials/published', views.tutorial_list_published),
    
]