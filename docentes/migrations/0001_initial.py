# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('wl_week', models.IntegerField()),
                ('wl_max', models.IntegerField()),
                ('Type', models.IntegerField()),
                ('situation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Actvity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('date_ini', models.DateField()),
                ('date_term', models.DateField()),
                ('comment', models.TextField()),
                ('actv_type', models.ForeignKey(to='docentes.ActivityType')),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
                ('addr_street', models.CharField(max_length=50)),
                ('addr_no', models.CharField(max_length=50)),
                ('addr_neighbour', models.CharField(max_length=50)),
                ('addr_city', models.CharField(max_length=50)),
                ('addr_uf', models.CharField(max_length=50)),
                ('addr_ZIP', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.URLField(max_length=50)),
                ('situation', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('wl_teaching', models.IntegerField()),
                ('wl_extres', models.IntegerField()),
                ('situation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
                ('coord', models.CharField(max_length=50)),
                ('situation', models.BooleanField()),
                ('campus', models.ForeignKey(to='docentes.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='CourseGrid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_init', models.DateField()),
                ('date_term', models.DateField()),
                ('situation', models.BooleanField()),
                ('course', models.ForeignKey(to='docentes.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
                ('ementa', models.TextField()),
                ('block', models.IntegerField()),
                ('work_load', models.IntegerField()),
                ('situation', models.BooleanField()),
                ('course', models.ForeignKey(to='docentes.Course')),
                ('course_grid', models.ForeignKey(to='docentes.CourseGrid')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=15)),
                ('contract_term', models.TextField()),
                ('effective', models.BooleanField()),
                ('situation', models.BooleanField()),
                ('contract', models.ForeignKey(to='docentes.ContractType')),
                ('course', models.ForeignKey(to='docentes.Course')),
            ],
            options={
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.AddField(
            model_name='actvity',
            name='teacher',
            field=models.ForeignKey(to='docentes.Teacher'),
        ),
    ]
