from django.urls import path
from . import views

urlpatterns = [
    path('',views.produit,name='produit'),
    path('ajout_produit/',views.ajouter_produit,name='ajout_produit'),
    path('modifier_produit/<str:pk>',views.modifier_produit,name='modifier_produit'),
    path('supprimer_produit/<str:pk>',views.supprimer_produit,name='supprimer_produit'),
]