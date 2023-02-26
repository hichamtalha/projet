
from django.db import models
from produit.models import Produit
from client.models import Client

# Create your models here.

class Credit(models.Model):
    ETAT=(('non payé','non payé'),('payé','payé'))
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    montant_credit=models.FloatField()
    date_credit=models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    etat=models.CharField(max_length=200,null=True,choices=ETAT)
    
    def __str__(self):
        return self.etat








