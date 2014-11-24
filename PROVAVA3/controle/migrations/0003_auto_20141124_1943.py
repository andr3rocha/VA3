# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_acesso'),
    ]

    operations = [
        migrations.CreateModel(
            name='lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeLugar', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Lugar')),
                ('nivelacesso', models.ForeignKey(verbose_name=b'Nivel de Acesso', to='controle.acesso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='nivelacesso',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nivel de Acesso'),
        ),
    ]
