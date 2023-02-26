from django.urls import path
from . import views

urlpatterns = [
    path('',views.credit,name='crd'),
    path('ajout_credit/',views.ajouter_credit,name='ajout_credit'),
    path('modifier_credit/<str:pk>',views.modifier_credit,name='modifier_credit'),
    path('supprimer_credit/<str:pk>',views.supprimer_credit,name='supprimer_credit'),


]