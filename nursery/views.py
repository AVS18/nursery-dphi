from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from .models import Plant
from customer.models import Order

def checkAuth(request):
    if request.user.is_authenticated == False:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Credentials')
        return redirect('/')
    else:
        return True
# Create your views here.
def dashboard(request):
    if checkAuth(request):
        return render(request,'nursery/dashboard.html')

def addPlants(request):
    if request.method=="POST":
        name=request.POST["name"]
        myfiles=request.FILES 
        image=myfiles["image"]
        price=request.POST["price"]
        Plant.objects.create(name=name,image=image,price=price,created_by=request.user)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Plant Added Successfully')
    obj = Plant.objects.filter(created_by=request.user)
    return render(request,"nursery/addPlants.html",{'obj':obj})

def viewOrder(request):
    obj = Order.objects.filter(product__created_by=request.user)
    return render(request,"nursery/viewOrder.html",{'obj':obj})