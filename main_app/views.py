from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# our Imports #333

from .models import Post, CURRENT_CITY, Profile, City
from .forms import Profile_Form, Post_Form

########### USER CREATION ##################


def home(request):
    err = ''
    err2 = ''
    if request.method == 'POST':
        # user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'] )
        form = Profile_Form(request.POST)
        if form.is_valid():
            try:
                new_profile = form.save(commit=False)
                user = User.objects.create_user(
                    request.POST['username'], request.POST['email'], request.POST['password'])
                user.first_name = request.POST['name']
                user.save()
                new_profile.user = user
                new_profile.save()
                login(request, user)
                send_mail('Welcome to Wayfair!', 'Hello', 'wwayfair82@gmail.com',
                          [request.POST['email']], fail_silently=False)
                return redirect('profile')
            except:
                err = "This profile already exists!"
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                context = {'form': form, "err2": "Wrong Username or Password"}
                return render(request, 'home.html', context)
    form = Profile_Form()
    context = {'form': form, "err": err}
    return render(request, 'home.html', context)


######## PROFILE PAGE ############


def profile(request):
    print(request.user.pk)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        print(request.FILES)
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=request.user)
        form = Profile_Form(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            profile.current_city = new_form.current_city
            profile.save()
        else:
            user.first_name = request.POST['name']
            user.save()
        return redirect('profile')
    form = Profile_Form()
    posts = Profile.objects.get(user=request.user).post_set.all()
    img = profile.img
    city = FindCity(profile.current_city)
    context = {'user': request.user, 'form': form,
               "posts": posts, 'city': city, 'img': img}
    return render(request, 'profile.html', context)

# Cities Routes (Temp)


#######  Vewing ALL the Citys ######


@login_required
def view_cities(request, city_name):
    posts = Post.objects.all().order_by('-date')
    city = []
    if request.method == 'POST':
        form = Post_Form(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.current_city = RiverceCity(request.POST['city'])
            profile = Profile.objects.get(user=request.user)
            new_post.profile = profile
            new_post.save()
    city_name = RiverceCity(city_name)

    for post in posts:
        if post.current_city == city_name:
            city.append(post)
    form = Post_Form()
    city_full_name = FindCity(city_name)
    context = {"city": city, 'form': form, 'city_name': city_full_name,
               'city_code': city_name, 'country': find_country(city_full_name)}
    return render(request, 'cities.html', context)


def img_upload(request):
    profile = Profile.objects.get(user=request.user)
    fs = FileSystemStorage()
    img_file = request.FILES['img']
    fs.save(img_file.name, img_file)
    profile.img = request.FILES['img']
    profile.save()
    return redirect('profile')


#### VIEWING a SPECIFIC POST ######

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post, 'city': FindCity(
        post.current_city), "city_code": post.current_city}
    return render(request, 'show_post.html', context)

##### LOGING OUT #####


def logout(request):
    auth.logout(request)
    return redirect('home')


##### DELETE  A POST ########

@login_required
def delete(request, post_id, city_name):
    post = Post.objects.get(id=post_id)
    # compare users
    if request.user.username == post.profile.user.username:
        Post.objects.get(id=post_id).delete()
        city_name = FindCity(city_name)
        return redirect('cities', city_name=city_name)
    # else TODO: 404 page
    return redirect('404.html')

##### EDIT A POST #######


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    # compare users
    if request.user.username != post.profile.user.username:
        Post.objects.get(id=post_id)
        # TODO 404 page
        return redirect('404.html')
    if request.method == 'POST':
        changed_post = Post_Form(request.POST, instance=post)
        if changed_post.is_valid():
            changed_post.save()
            return redirect('post', post_id=post_id)
    form = Post_Form(instance=post)
    context = {'form': form, 'post_id': post_id,
               'post': post, 'city': FindCity(post.current_city)}
    return render(request, 'edit_post.html', context)


def test(request, city_name):
    pass


####### Custom functions ######

def find_country(city):
    if city == 'London':
        return 'United Kingdom'
    elif city == 'Sydney':
        return 'Australia'
    elif city == 'San Francisco':
        return 'United States'
    elif city == 'Seattle':
        return 'United States'


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
    elif city == 'San Francisco' or city == 'San_Francisco':
        return 'SFO'
    elif city == 'Seattle':
        return 'SEA'
