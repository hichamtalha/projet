# Generated by Django 4.1.7 on 2023-02-25 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0011_remove_commande_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='prix',
        ),
    ]