# Generated by Django 4.0.6 on 2022-08-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmashop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=200),
            preserve_default=False,
        ),
    ]