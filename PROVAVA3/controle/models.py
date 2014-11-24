#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino'),

]
class acesso(models.Model):
	nivelacesso = models.CharField('Nivel de Acesso',max_length=100,null=True)
	def __unicode__(self):
		return self.nivelacesso

class Pessoa(models.Model):
	
	Nome = models.CharField('Nome',max_length=100,null=True)
	nivelacesso = models.ForeignKey(acesso,verbose_name="Nivel de Acesso",null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=14,unique=True,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=STATE_CHOICES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)	

 	
 	def __unicode__(self):
		return self.Nome


class lugar(models.Model):
	NomeLugar = models.CharField('Nome do Lugar',max_length=100,null=True)
	nivelacesso = models.ForeignKey(acesso,verbose_name="Nivel de Acesso",null=True)
	
	def __unicode__(self):
		return self.NomeLugar

class validacao(models.Model):
	nivelacesso = models.ForeignKey(acesso,verbose_name="Nivel de Acesso",null=True)
	Nome = models.ForeignKey(Pessoa,verbose_name="Nome",null=True)
	NomeLugar = models.ForeignKey(lugar,verbose_name="Nome do Lugar",null=True)
	Entrada = models.DateTimeField('Registro Entrada',null=True)
	Saida = models.DateTimeField('Registro Saida',null=True)
	
	#def clean(self):
		#q = nivelacesso.objects.filter(nivelacesso=self.acesso,nome=self.Pessoa)
		#if not q:
			#raise ValidationError("Pessoa não autorizada")
	
	


	
