from django.db import models

# Create your models here.
class Users(models.Model):
    UserName = models.CharField(max_length=100,unique=True)
    Password = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    Pic = models.ImageField()
    def __str__(self):
        return "{}".format(self.UserName)