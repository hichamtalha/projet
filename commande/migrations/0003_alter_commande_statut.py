# Generated by Django 4.1.7 on 2023-02-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_commande_client_commande_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200),
        ),
    ]