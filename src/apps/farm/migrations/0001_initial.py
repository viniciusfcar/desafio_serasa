# Generated by Django 5.1.5 on 2025-01-29 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name_farm', models.CharField(max_length=300, verbose_name='Nome da Fazenda/Propriedade')),
                ('total_area_farm', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área Total')),
                ('agricultural_area', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área Agricultável')),
                ('vegetation_area', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área de Vegetação')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_address', to='address.addressfarmmodel', verbose_name='Endereço da Fazenda')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_farmer', to='farmer.farmermodel', verbose_name='Agricultor')),
            ],
            options={
                'verbose_name': 'Fazenda',
                'verbose_name_plural': 'Fazendas',
                'db_table': 'farm',
            },
        ),
    ]
