from django.shortcuts import render,redirect
from .forms import CreditForm
from .models import Credit
from client.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def credit(request):
    credits=Credit.objects.all()
    clients=Client.objects.all()
    context={'clients':clients,'credits':credits}
    return render(request,'credit/credit.html',context)


def ajouter_credit(request):
    form=CreditForm()
    if request.method=='POST':
        form=CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'credit/ajouter_credit.html',context)

def modifier_credit(request,pk):
    credit=Credit.objects.get(id=pk)
    form=CreditForm(instance=credit)
    if request.method=='POST':
        form=CreditForm(request.POST,instance=credit)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'credit/ajouter_credit.html',context)

def supprimer_credit(request,pk):
    credit=Credit.objects.get(id=pk)
    if request.method=='POST':
        credit.delete()
        return redirect('/')
    context={'item':credit}
    return render(request,'credit/supprimer_credit.html',context)

