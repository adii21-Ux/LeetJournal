from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as logout_user

def registerUser(request):
    form = RegisterUserForm()
    
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registered Successfully")
            return redirect('user:loginuser')
        else:
            messages.error(request, "Failed to register user")
    else:
        messages.error(request,"Invalid User credentials")
                
    context = {'form':form}
    return render(request, 'user/registration.html', context)

def loginUser(request):
    if request.method=="POST":
        forms = AuthenticationForm(request, data = request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                print("here")
                login(request, user)
                messages.success(request, 'User Logged in successfully')
                return redirect("core:homepage")
            else:
                messages.error(request, "User login failed")
        else:
            messages.error(request, "Invalid user credentials")
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form})
        

def logout(request):
    logout_user(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("user:loginuser")