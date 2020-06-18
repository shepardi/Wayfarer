from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
#user.first_name = 'John'
#user.last_name = 'Citizen'
#user.save()

# Create your views here.

from  .models import Post, CURRENT_CITY, Profile
from  .forms import Profile_Form

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


def test(request):
  if request.method== 'POST' :  
    form = Profile_Form(request.POST)
    if form.is_valid():
      new_profile = form.save(commit=False)
      user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'] )
      user.first_name=request.POST['name']
      user.save()
      new_profile.user=user
      new_profile.save()
      login(request,user)
      return redirect('testprofile')
    else:
      username=request.POST['username']
      password=request.POST['password']
      user=  authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect('testprofile')
      else:
        return render(request, 'test.html', context)
  form = Profile_Form()
  context = {'form': form }
  return render(request, 'test.html', context)



def testprofile(request):
  if request.method=='POST':
    form = Profile_Form(request.POST)
    if form.is_valid():
      city_change=form.save(commit=False)
      profile = Profile.objects.get(user = request.user)
      
      profile.current_city=form
      profile.save()
    else:    
      user = User.objects.get(username = request.user.username)
      user.first_name=request.POST['name']
      user.save()
    return redirect('testprofile')
  form = Profile_Form()
  posts = Profile.objects.get(user=request.user).post_set.all()
  city= Profile.objects.get(user=request.user).current_city
  city=FindCity(city)

  context={'user':request.user , 'posts':posts , 'city' : city ,'form' :form }
  return render(request, 'testprofile.html', context)



def FindCity(city):
  if city == 'LDN':
    return 'London'
  elif city == 'SYD':
    return 'Sydney'
  elif city == 'SFO':
    return 'San Francisco'
  elif city == 'SEA':
    return 'Seattle'


def RiverceCity(city):
  if city == 'London':
    return 'LDN'
  elif city == 'Sydney':
    return 'SYD'
  elif city == 'San Francisco':
    return 'SFO'
  elif city == 'Seattle':
    return 'SEA'