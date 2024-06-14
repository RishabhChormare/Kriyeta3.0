from django.urls import path
from . import views
# from .views import read 

urlpatterns = [
    path('', views.index),
    path('docnur/', views.doctor_nurse, name='doctor_nurse'),
    path('about/', views.about, name='about'),
    path('admin/', views.admin, name='admin'),
    
]