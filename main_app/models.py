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
  
  def __str__(self):
        return self.user.username
  
class Post(models.Model):
  title = models.CharField(max_length=100)
  current_city = models.CharField(max_length=3, choices=CURRENT_CITY, default=CURRENT_CITY[0][0])
  description = models.TextField(max_length=1000)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  date = models.DateTimeField( auto_now_add=True )
  
  def __str__(self):
    return self.title 


class City(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)


