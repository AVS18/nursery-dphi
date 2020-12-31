from django.db import models
from nursery.models import Plant
from base.models import User
# Create your models here.
class Cart(models.Model):
    items = models.ForeignKey(Plant,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    product = models.ForeignKey(Plant,on_delete=models.DO_NOTHING)
    ordered_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    ordered_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=1000)