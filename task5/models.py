from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()

    def __str__(self):
        return self.username