from django.forms import ModelForm
from produit.models import Produit  

class ProduitForm(ModelForm):  
    class Meta:  
        model=Produit
        fields = "__all__" 