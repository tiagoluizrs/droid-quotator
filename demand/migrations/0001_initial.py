# Generated by Django 2.2.3 on 2019-07-27 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('delivery_address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('comp', models.CharField(max_length=20, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=40, verbose_name='Cidade')),
                ('contact_tel', models.CharField(max_length=20, verbose_name='Telefone')),
                ('contact_email', models.CharField(max_length=70, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de edição')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
