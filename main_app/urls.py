from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('logout/', views.logout, name='logout'),
  path('post/<int:post_id>', views.view_post, name='post'),
  path('cities/', views.view_cities, name='cities')

]