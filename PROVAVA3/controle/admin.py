#coding:utf-8
from django.contrib import admin
from models import Pessoa,lugar,validacao

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	
	list_display = ['Nome','CPF']
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']

class lugarAdmin(admin.ModelAdmin):
	list_display = ['NomeLugar','nivelacesso']
	list_filter = ['NomeLugar']
	search_fields = ['NomeLugar','nivelacesso']

class validacaoAdmin(admin.ModelAdmin):
	list_display = ['lugar','Pessoa','Entrada','Saida']
	list_filter = ['lugar','Pessoa','Entrada','Saida']
	search_fields = ['lugar','Pessoa','Entrada','Saida']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(lugar,lugarAdmin)
admin.site.register(validacao,validacaoAdmin)
