# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Demand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    delivery_address = models.CharField(max_length=100, verbose_name='Endereço')
    number = models.IntegerField(verbose_name='Número')
    comp = models.CharField(max_length=20, verbose_name='Complemento', null=True, blank=True)
    cep = models.CharField(max_length=10, verbose_name='CEP')
    state = models.CharField(max_length=40, verbose_name='Estado')
    city = models.CharField(max_length=40, verbose_name='Cidade')
    contact_tel = models.CharField(max_length=20, verbose_name='Telefone')
    contact_email = models.CharField(max_length=70, verbose_name='E-mail')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de edição')
    status = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.name