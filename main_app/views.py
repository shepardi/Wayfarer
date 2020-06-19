from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth


#user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
# Update fields and then save again
#user.first_name = 'John'
#user.last_name = 'Citizen'
#user.save()
# Create your views here.


from  .models import Post, CURRENT_CITY, Profile
from .forms import Profile_Form


########### USER CREATION ##################


def home(request):
  err = ''
  err2 = ''
  if request.method == 'POST' :  
    # user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'] )
    form = Profile_Form(request.POST)
    if form.is_valid():
      try:
        new_profile = form.save(commit=False)
        user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'] )
        user.first_name=request.POST['name']
        user.save()
        new_profile.user=user
        new_profile.save()
        login(request,user)
        return redirect('profile')
      except:
        err="ALREADY MADE THIS PROFILE"
    else:
      username=request.POST['username']
      password=request.POST['password']
      user= authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect('profile')
      else:
        context = {'form': form, "err2": "Wrong username or Pass"}
        return render(request, 'home.html', context)
  form = Profile_Form()
  context = {'form': form , "err":err }
  return render(request, 'home.html', context)


def profile(request):
  if request.method=='POST':
      user = User.objects.get(username = request.user.username)
      form = Profile_Form(request.POST)
      if form.is_valid(): 
        new_form=form.save(commit=False)
        profile =  Profile.objects.get(user=request.user)
        profile.current_city = new_form.current_city
        profile.save()
      else:
        user.first_name=request.POST['name']
        user.save()
      return redirect('profile')
  form = Profile_Form()
  posts = Profile.objects.get(user=request.user).post_set.all()
  city= Profile.objects.get(user=request.user).current_city
  city=FindCity(city)
  context={'user':request.user, 'form' :form , "posts" : posts , 'city' : city }
  return render(request, 'profile.html', context)

# Cities Routes (Temp)
def view_cities(request):
  return render(request, 'cities.html')


def view_post(request , post_id):
  post=Post.objects.get(id=post_id)
  context={"post":post, 'city': FindCity(post.current_city)  }
  return render(request, 'show_post.html', context)

  
def logout(request):
  auth.logout(request)
  return redirect('home')


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