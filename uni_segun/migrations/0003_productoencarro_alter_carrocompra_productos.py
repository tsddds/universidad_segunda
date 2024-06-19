# Generated by Django 5.0.6 on 2024-06-10 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_segun', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoEnCarro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_segun.carrocompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_segun.producto')),
            ],
        ),
        migrations.AlterField(
            model_name='carrocompra',
            name='productos',
            field=models.ManyToManyField(through='uni_segun.ProductoEnCarro', to='uni_segun.producto'),
        ),
    ]
