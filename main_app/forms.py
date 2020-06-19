from django.forms import ModelForm,PasswordInput
from .models import Profile 


class Profile_Form(ModelForm):
    class Meta:
        model= Profile
        fields=['current_city']