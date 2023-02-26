from django.shortcuts import render,HttpResponse,redirect
from .forms import ClientForm
from .models import Client
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required(login_url='login')

def client(request):
    return render(request,'client/list_client.html')

def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    total_credit = client.credit_set.aggregate(Sum('montant_credit'))['montant_credit__sum']
    commande_total=commande.count()
    context={'client':client,'commande':commande,'commande_total':commande_total,'total_credit':total_credit}
    return render(request,'client/list_client.html',context)

def ajouter_client(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'client/ajouter_client.html',context)

def modifier_client(request,pk):
    client=Client.objects.get(id=pk)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'client/ajouter_client.html',context)

def supprimer_client(request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/')
    context={'item':client}
    return render(request,'client/supprimer_client.html',context)