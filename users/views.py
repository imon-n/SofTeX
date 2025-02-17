from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from .form import RegisterForm

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/signup.html',{'form': form})

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)

            if user is not None:
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')
