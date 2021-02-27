from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    booked_by = models.CharField(max_length=30, blank=True)
    status = models.BooleanField(default=1)
    file = models.FileField(upload_to='files/')


