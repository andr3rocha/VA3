#coding:utf-8
from django.contrib import admin
from models import Pessoa, lugar, validacao

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	
	list_display = ['Nome','CPF']
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']

class lugarAdmin(admin.ModelAdmin):
	list_display = ['NomeLugas','nivelacesso']
	list_filter = ['NomeLugar']
	search_fields = ['NomeLugar','nivelacesso']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(lugar)
admin.site.register(validacao)
