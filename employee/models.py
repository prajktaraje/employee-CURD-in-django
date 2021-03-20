from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=122,default='')
    email=models.EmailField(max_length=122,default='')
    password=models.CharField(max_length=122,default='')
    

    def __str__(self):
        return self.name