# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo:')),
                ('url', models.SlugField(help_text='URL baseada no t\xedtulo.', max_length=200, unique=True, verbose_name='URL')),
                ('pub_date', models.DateTimeField(verbose_name='Data de publica\xe7\xe3o:')),
                ('conteudo', models.TextField(verbose_name='Conte\xfado da p\xe1gina:')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artigos.Agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autores',
            field=models.ManyToManyField(to='artigos.Autor'),
        ),
    ]