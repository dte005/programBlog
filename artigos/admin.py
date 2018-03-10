# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from artigos.models import Agencia, Autor, Artigo

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','email')
    search_fields = ('nome','email')
    ordering = ('nome',)

class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome','site')

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'tipo', 'pub_date')
    search_fields = ('pub_date',)
    ordering=('-pub_date',)
    prepopulated_fields = {'url': ('titulo',)}
    filter_horizontal = ('autores',)


admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
