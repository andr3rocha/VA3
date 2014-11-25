#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.core.exceptions import ValidationError

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino'),

]
NIVEL_ACESSO = [

	(1,'Livre'),
	(2,'Restrito'),
	(3,'Reservado')

]

class Pessoa(models.Model):
	
	Nome = models.CharField('Nome',max_length=100,null=True)
	nivelacesso = models.IntegerField('Nivel de Acesso',choices=NIVEL_ACESSO,null=True)
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
	nivelacesso = models.IntegerField('Nivel de Acesso',choices=NIVEL_ACESSO,null=True)
	
	def __unicode__(self):
		return self.NomeLugar

class validacao(models.Model):
	lugar = models.ForeignKey(lugar,verbose_name='Lugar de Acesso')
	Pessoa = models.ForeignKey(Pessoa,verbose_name="Pessoa")
	Entrada = models.DateTimeField('Registro Entrada',auto_now=True,null=True)
	Saida = models.DateTimeField('Registro Saida',blank=True,null=True)
	
	def __unicode__(self):
		return "%s - %s"% (self.Pessoa,self.lugar)
	
	def clean (self):
		
		q = validacao.objects.filter(Pessoa=self.Pessoa,Saida__isnull=True)
		if q and self.id == None:
			raise ValidationError("Usuario Ja se encontra em outro Lugar")
		
		if self.lugar.nivelacesso > self.Pessoa.nivelacesso:
			raise ValidationError ("Usuario sem Permissão de acesso")
		
	
	
	
	
	
	


	
