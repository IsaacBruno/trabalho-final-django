# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Curso'},
        ),
        migrations.AlterModelOptions(
            name='coursegrid',
            options={'verbose_name_plural': 'Grade Curricular'},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name_plural': 'Discplina'},
        ),
    ]
