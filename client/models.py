from django.db import models



# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=100)
    addresse = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    date_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
