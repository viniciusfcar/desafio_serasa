# Generated by Django 5.1.5 on 2025-01-29 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HarvestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Safra')),
                ('year', models.CharField(max_length=4, verbose_name='Ano da Safra')),
            ],
            options={
                'verbose_name': 'Safra',
                'verbose_name_plural': 'Safras',
                'db_table': 'harvest',
            },
        ),
    ]
