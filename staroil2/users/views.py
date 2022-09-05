import errno
from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import is_valid_path
from django.contrib.auth.decorators import login_required

from users.form import UserForm

@login_required
def logout_user(request):
    logout(request)
    redirect('home')

def home(request):
    error=''
    if request.method == "POST":
        #MyLoginForm = LoginForm(request.POST)
        username = request.POST['username']
        request.session['username'] = username
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_directeur:
                return redirect('directeur')
            
            elif user.is_chef_secteur:
                return redirect('chef_secteur')
            else:
                return redirect('utilisateur')
        else:
            error = 'password ou username est incorrect'
            
    return render(request, 'login.html', {'error':error})
    #return render(request, 'login.html')


def register(request):
    form = UserForm()
    if request.method == "POST":  
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'register.html', {'form': form})
            

def directeur(request):
    return render(request, 'directeur.html')

def chef_secteur(request):
    return render(request, 'chef_secteur.html')

def utilisateur(request):
    return render(request, 'utilisateur.html')

# def prediction(request):
#     return render(request, 'prediction.html')
