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
  name = models.CharField(max_length=100)
  current_city = models.CharField(max_length=3, choices=CURRENT_CITY, default=CURRENT_CITY[0][0])
  join_date = models.DateField(default=date.today())
  
  


