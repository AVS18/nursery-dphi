from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from base.models import User
# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj = authenticate(username=username,password=password)
        if obj is not None:
            auth.login(request,obj)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Login Success')
            if request.user.account_type == "Customer":
                return redirect('/customer/dashboard')
            elif request.user.account_type == "Nursery":
                return redirect('/nursery/dashboard')
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Invalid Request')
    return redirect('/')    

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        account_type=request.POST["account_type"]
        obj = User.objects.create_user(first_name=first_name,email=email,username=username,password=password,account_type=account_type)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Registration Successful')
        return redirect('/')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid Request')
        return redirect('/')  

def logout(request):
    auth.logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Logout Successful')    
    return redirect('/')      