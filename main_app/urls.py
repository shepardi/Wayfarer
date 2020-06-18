from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('test/', views.test, name='test'),
  path('testprofile/', views.testprofile, name='testprofile'),


]