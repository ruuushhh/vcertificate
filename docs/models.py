from django.db import models
from django.contrib.auth.models import User


class cer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    issue_year = models.DateField(null=True, blank=True)
    files = models.FileField(upload_to='')
    activity = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
