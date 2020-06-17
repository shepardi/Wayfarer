from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
  form = UserCreationForm()
  context = {'form': form}
  return render(request, 'home.html', context)

