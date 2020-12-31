from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    account_type = models.CharField(max_length=10,choices=(("Nursery","Nursery"),("Customer","Customer")))