from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home view
def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error. Please try again.")
            return render(request, 'home.html', {})
    else:
    	return render(request, 'home.html', {})
# Login view (optional)
# def login_user(request):
#     return render(request, 'login.html', {})  # Optional placeholder

# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
def register_user(request):
	return render(request,'register.html',{})

