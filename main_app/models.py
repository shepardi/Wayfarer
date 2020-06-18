from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

from datetime import date

CURRENT_CITY = (
  ('LDN', 'London'),
  ('SYD', 'Sydney'),
  ('SFO', 'San Francisco'),
  ('SEA', 'Seattle'),
)

class Profile(models.Model):
  current_city = models.CharField(max_length=3, choices=CURRENT_CITY, default=CURRENT_CITY[0][0])
  user=models.ForeignKey(User, on_delete=models.CASCADE, default='1')
  
class Post(models.Model):
  title = models.CharField(max_length=100)
  current_city = models.CharField(max_length=3, choices=CURRENT_CITY, default=CURRENT_CITY[0][0])
  description = models.TextField(max_length=250)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class City(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)


