from django.db import models


class User(models.Model):
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'users'
