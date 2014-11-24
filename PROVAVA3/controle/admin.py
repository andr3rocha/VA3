#coding:utf-8
from django.contrib import admin
from models import Pessoa, acesso, lugar, validacao

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	
	list_display = ['Nome','CPF']
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']

class acessoAdmin(admin.ModelAdmin):
	
	list_display = ['nivelacesso','horachegada','horasaida']
	list_filter = ['nivelacesso']
	search_fields = ['nivelacesso', 'horachegada', 'horasaida'] #faltanomedapessoa

class lugarAdmin(admin.ModelAdmin):
	list_display = ['NomeLugas','nivelacesso']
	list_filter = ['NomeLugar']
	search_fields = ['NomeLugar','nivelacesso']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(acesso)
admin.site.register(lugar)
admin.site.register(validacao)
