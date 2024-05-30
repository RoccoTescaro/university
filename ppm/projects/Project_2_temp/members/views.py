from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return render(request, 'home.html', { })
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def signinUser(request):
    form = forms.SigninForm()
    if request.method == 'POST':
        form = forms.SigninForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = first_name + last_name
            password = form.cleaned_data.get('password1')
            #password2 = form.cleaned_data.get('password2')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')
    
    return render(request, 'signin.html', {'form': form } )
