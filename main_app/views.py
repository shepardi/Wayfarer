from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from  .models import Post, CURRENT_CITY, Profile


########### USER CREATION ##################

def home(request):
  if request.method== 'POST' :
    form= UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request,user)
      return redirect('profile')
  else: 
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'home.html', context)

def profile(request):
  posts= Post.objects.all()
  #user= Profile.objects.get(name=request.user.username)
  city=[]
  for town in CURRENT_CITY:
    city.append(town[1])

  context={'posts':posts , "city" : city , "user":request.user} 
  return render(request, 'profile.html', context)
