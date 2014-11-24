# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_auto_20141124_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nivelacesso',
            field=models.ForeignKey(verbose_name=b'Nivel de Acesso', to='controle.acesso', null=True),
            preserve_default=True,
        ),
    ]
