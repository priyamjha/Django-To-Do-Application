from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm
from django.contrib.auth.models import User




def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for registering. Please log in.')
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.warning(request, error)
            return redirect('register')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username exists
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                # Incorrect password or inactive account
                messages.warning(request, 'Incorrect password or inactive account.')
        else:
            # Username does not exist
            messages.warning(request, 'Username does not exist.')
        
        return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has been ended. Please log in to continue')
    return redirect('login')