# Generated by Django 2.2.3 on 2019-07-31 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sobrenome')),
                ('active', models.BooleanField(default=True, help_text='Estado do usuário ativo/inativo')),
                ('staff', models.BooleanField(default=False, help_text='Caso seja marcado o usuário terá acesso ao painel admin')),
                ('admin', models.BooleanField(default=False, help_text='Administrador do sistema')),
                ('role', models.CharField(choices=[('1', 'Admin'), ('2', 'Anunciante')], default='1', max_length=1, verbose_name='Função')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]