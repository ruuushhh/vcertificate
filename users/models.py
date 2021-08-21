from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    year = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return self.f_name
