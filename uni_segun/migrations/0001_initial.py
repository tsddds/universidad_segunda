# Generated by Django 5.0.1 on 2024-06-07 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('academia', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
                ('numero_de_telefono', models.CharField(max_length=15, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_segun.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=16)),
                ('fecha_expiracion', models.DateField()),
                ('codigo_seguridad', models.CharField(max_length=4)),
                ('tipo_tarjeta', models.CharField(max_length=50)),
                ('nombre_tarjeta', models.CharField(max_length=225)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_segun.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='CarroCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productos', models.ManyToManyField(to='uni_segun.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_segun.usuario')),
            ],
        ),
    ]
