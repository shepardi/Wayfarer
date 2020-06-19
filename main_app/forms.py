from django.forms import ModelForm,PasswordInput
from .models import Profile, Post


class Profile_Form(ModelForm):
    class Meta:
        model= Profile
        fields=['current_city']


class Post_Form(ModelForm):
    class Meta:
        model=Post
        fields=['title','description',]