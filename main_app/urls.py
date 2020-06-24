# Django Confings

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Our Imports

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('upload_img/', views.img_upload, name='img_upload'),
    path('post/<int:post_id>', views.view_post, name='post'),
    path('cities/<str:city_name>', views.view_cities, name='cities'),
    path('test/<str:city_name>', views.test, name='test'),
    path('edit/<int:post_id>', views.edit_post, name='edit'),
    path('test/<str:city_name>/delete/<int:post_id>', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
