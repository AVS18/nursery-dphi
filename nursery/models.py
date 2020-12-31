from django.db import models
from base.models import User
# Create your models here.
class Plant(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='plant_pics')
    price=models.IntegerField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)