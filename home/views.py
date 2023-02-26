
from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from credit.models import Credit
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    credits=Credit.objects.all()
    context={'commandes':commandes,'clients':clients,'credits':credits}
    return render(request,'home/acceuil.html',context)

