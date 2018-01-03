# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0002_auto_20171207_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contracttype',
            options={'verbose_name_plural': 'Tipo de Contrato'},
        ),
    ]
