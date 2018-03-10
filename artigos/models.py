# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

escolhas = (
    ("Python", "python"),
    ("Linux", "linux"),
    ("Javascript", "javascript"),
    ("PHP", "php"),
    ("Java", "java"),
    ("Jquery", "jquery"),
    ("Django", "django"),)

class Agencia(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()

    #def __str__(self):
    #    return nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

class Artigo(models.Model):
    titulo = models.CharField('Titulo:',max_length=80)
    url = models.SlugField(
            'URL',
            max_length=200,
            help_text='URL baseada no título.',
            unique=True)
    tipo = models.CharField('Tipo', max_length=9, choices=escolhas, default="Python")
    pub_date = models.DateTimeField('Data de publicação:')
    conteudo = models.TextField('Conteúdo da página:')
    autores = models.ManyToManyField(Autor)
    agencia = models.ForeignKey(Agencia)
