from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from nursery.models import Plant
from .models import Cart,Order

def dashboard(request):
    return render(request,'customer/dashboard.html')

def filter():
    return Plant.objects.all().values_list('name',flat=True).distinct()

def viewPlant(request):
    if request.method=="POST":
        name=request.POST["name"]
        obj = Plant.objects.filter(name=name)
        return render(request,"customer/viewPlant.html",{'obj':obj,'distinct':filter()})
    obj = Plant.objects.all()
    return render(request,"customer/viewPlant.html",{'obj':obj,'distinct':filter()})

def addCart(request,pid):
    plant_requested=Plant.objects.get(id=pid)
    obj = Cart.objects.create(items=plant_requested,quantity=1,created_by=request.user)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Order Added Successfully. Click on view cart')
    return redirect('/customer/viewPlant')

def viewCart(request):
    obj=Cart.objects.filter(created_by=request.user)
    if len(obj)==0:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'No Items added in Cart')
        return redirect('/customer/viewPlant') 
    else:
        return render(request,'customer/viewCart.html',{'obj':obj})

def removeItem(request,pid):
    Cart.objects.get(id=pid).delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Cart Updated Successfully')
    return redirect('/customer/viewCart')

def order(request):
    if request.method=="POST":
        obj = Cart.objects.filter(created_by=request.user)
        for item in obj:
            Order.objects.create(product=item.items,ordered_by=request.user,address=request.POST["address"])
            Cart.objects.get(id=item.id).delete()
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Order Placed Successfully. Items will be shipped to your provided address soon')
        return redirect('/customer/dashboard')
    obj = Order.objects.filter(ordered_by=request.user)    
    return render(request,"customer/viewOrder.html",{'obj':obj})