from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Products.models import Profil 

def home(request):
    return render(request, "home.html")

def Login(request):
    return render(request, 'Login.html')

def SignUp(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('Product_Login')
    return render(request, 'SignUp.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/Products')
        else:
            return redirect('Product_SignUp')


    return render(request, 'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('Login.html')

def contact(request):
    return render(request, "contact.html")

def Profils(request):
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        Cin_Number = request.POST.get('cin')
        phone_Number = request.POST.get('phone')
        address = request.POST.get('address')
        profil = Profil.objects.create(username=username, email=email, Cin_Number=Cin_Number, phone_Number=phone_Number,address=address)
        profil.save()
        return redirect('/Products')
    return render(request, 'profile.html',)