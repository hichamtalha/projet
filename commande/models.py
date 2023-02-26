
from django.db import models
from client.models import Client
from produit.models import Produit
# Create your models here.
class Commande(models.Model):
    STATUS=(('non payé','non payé'),('payé','payé'))
    client=models.ForeignKey(Client,null=True,on_delete=models.SET_NULL)
    produit=models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    quantite=models.IntegerField()
    statut=models.CharField(max_length=200,null=True,choices=STATUS)
    date_creation=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.statut
