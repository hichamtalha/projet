# Generated by Django 4.1.7 on 2023-02-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0003_alter_commande_statut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='statut',
        ),
        migrations.AddField(
            model_name='commande',
            name='quantite',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]