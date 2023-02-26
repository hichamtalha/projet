from django.db import models


# Create your models here.
class Categorie(models.Model):
    nom=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom=models.CharField(max_length=200,null=True)
    prix=models.FloatField(null=True)
    description = models.TextField()
    quantite=models.IntegerField()
    categorie=models.ManyToManyField(Categorie)






    def __str__(self):
        return self.nom