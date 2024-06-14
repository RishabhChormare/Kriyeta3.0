from django.urls import path
from . import views
from . views import read 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='index'),
    path('admin/', views.admin, name='index'),
]