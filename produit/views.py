from django.shortcuts import render,redirect
from .forms import ProduitForm
from django.http import HttpResponse
from produit.models import Produit
from .models import Categorie
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login') 

def produit(request):
    produits=Produit.objects.all()
    categories=Categorie.objects.all()
    context={'produits':produits,'categories':categories}
    return render(request,'produit/produit.html',context)

def ajouter_produit(request):
    form=ProduitForm()
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produit')
    context={'form':form}
    return render(request,'produit/ajouter_produit.html',context)

def modifier_produit(request,pk):
    produit=Produit.objects.get(id=pk)
    form=ProduitForm(instance=produit)
    if request.method=='POST':
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/produit')
    context={'form':form}
    return render(request,'produit/ajouter_produit.html',context)

def supprimer_produit(request,pk):
    produit=Produit.objects.get(id=pk)
    if request.method=='POST':
        produit.delete()
        return redirect('/produit')
    context={'item':produit}
    return render(request,'produit/supprimer_produit.html',context)
