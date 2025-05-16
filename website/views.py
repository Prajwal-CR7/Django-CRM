from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Home view
def home(request):
    records = Record.objects.all()
    for record in records:
        print(record.first_name, record.last_name)
    
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
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


# Register view
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})


# Customer record view
def customer_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
        except Record.DoesNotExist:
            messages.error(request, "Record not found.")
            return redirect('home')
    else:
        messages.error(request, "You must be logged in to view that page")
        return redirect('home')


# Delete record view
def delete_record(request, pk):
    if request.user.is_authenticated:
        try:
            record_to_delete = Record.objects.get(id=pk)
            record_to_delete.delete()
            messages.success(request, "The record was deleted successfully.")
        except Record.DoesNotExist:
            messages.error(request, "Record not found.")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to take action.")
        return redirect('home')


# Add record view
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Record added successfully")
				return redirect('home')
		return render(request, 'add_record.html', {'form': form})
	else:
		messages.error(request, "You must be logged in to add a record.")
		return redirect('home')
def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form =AddRecordForm(request.POST or None ,instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Updated  successfully!!")
			return redirect('home')
		else:
			return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
