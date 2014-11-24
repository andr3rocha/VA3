# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='acesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivelacesso', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'1', b'Livre'), (b'2', b'Restrito'), (b'3', b'Reservado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
