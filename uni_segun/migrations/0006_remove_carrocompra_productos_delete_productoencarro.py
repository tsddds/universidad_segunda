# Generated by Django 5.0.6 on 2024-06-10 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_segun', '0005_carrocompra_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrocompra',
            name='productos',
        ),
        migrations.DeleteModel(
            name='ProductoEnCarro',
        ),
    ]