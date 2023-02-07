from django.shortcuts import render,redirect,HttpResponse
from .form import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = CustomUserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login_user')
    else:        
        fm = CustomUserCreationForm()
        return render(request,'app1/signup.html',{"form":fm})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')    
        password = request.POST.get('password')
        student = authenticate(request,email=email,password=password)
        
        if student is not None:
            login(request,student)
            return redirect('profile')
        else:
           return HttpResponse('User name or password is incorrect')
    else:   
        return render(request,'app1/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def profile(request):
    return render(request,'app1/profile.html')
