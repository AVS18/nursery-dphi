from .models import User
from customer.models import Order
from nursery.models import Plant
from rest_framework import  serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff','first_name','account_type','password']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product','ordered_by','ordered_at','address']
        depth = 2

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['name','image','price']
