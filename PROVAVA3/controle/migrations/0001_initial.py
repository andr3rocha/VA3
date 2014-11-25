# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeLugar', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Lugar')),
                ('nivelacesso', models.IntegerField(null=True, verbose_name=b'Nivel de Acesso', choices=[(1, b'Livre'), (2, b'Restrito'), (3, b'Reservado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('nivelacesso', models.IntegerField(null=True, verbose_name=b'Nivel de Acesso', choices=[(1, b'Livre'), (2, b'Restrito'), (3, b'Reservado')])),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF')),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email')),
                ('Logradouro', models.CharField(max_length=100, null=True, verbose_name=b'Logradouro')),
                ('Numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('UF', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('CEP', models.CharField(max_length=9, null=True, verbose_name=b'CEP')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='validacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Entrada', models.DateTimeField(auto_now=True, verbose_name=b'Registro Entrada', null=True)),
                ('Saida', models.DateTimeField(null=True, verbose_name=b'Registro Saida', blank=True)),
                ('Pessoa', models.ForeignKey(verbose_name=b'Pessoa', to='controle.Pessoa')),
                ('lugar', models.ForeignKey(verbose_name=b'Lugar de Acesso', to='controle.lugar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
