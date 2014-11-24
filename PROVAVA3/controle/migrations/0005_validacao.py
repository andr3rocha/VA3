# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_pessoa_nivelacesso'),
    ]

    operations = [
        migrations.CreateModel(
            name='validacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Entrada', models.DateTimeField(null=True, verbose_name=b'Registro Entrada')),
                ('Saida', models.DateTimeField(null=True, verbose_name=b'Registro Saida')),
                ('Nome', models.ForeignKey(verbose_name=b'Nome', to='controle.Pessoa', null=True)),
                ('NomeLugar', models.ForeignKey(verbose_name=b'Nome do Lugar', to='controle.lugar', null=True)),
                ('nivelacesso', models.ForeignKey(verbose_name=b'Nivel de Acesso', to='controle.acesso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
