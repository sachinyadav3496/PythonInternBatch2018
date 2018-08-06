from django.db import models

class Users(models.Model):
    User_Name = models.CharField(max_length=100,unique=True)
    Password = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    def __str__(self):
        return self.User_Name
