from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def loginPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')

    return render(request,'compte/login.html',context)

def lougoutUser(request):
    logout(request)
    return redirect('login')

