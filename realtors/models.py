from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    description=models.TextField(blank=True)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now, blank=True)
    
    #this is to show the name of the realtor when we add it via admin panel otherwise
    #it will show object 1 or something weirdly
    def __str__(self):
        return self.name    
    