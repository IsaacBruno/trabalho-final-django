#encoding: utf-8

from __future__ import unicode_literals
from django.db import models

#CAMPUS
class Campus(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    addr_street = models.CharField(max_length=50)
    addr_no = models.CharField(max_length=50)
    addr_neighbour = models.CharField(max_length=50)
    addr_city = models.CharField(max_length=50)
    addr_uf = models.CharField(max_length=50)
    addr_ZIP = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.EmailField()
    site = models.URLField(max_length=50)    
    situation = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Campus"
#CURSO
class Course(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    coord = models.CharField(max_length=50)
    situation = models.BooleanField()

    def __unicode__(self):
        return self.name + ' - ' + self.campus.name
    class Meta:
        verbose_name_plural = "Curso"    
        
#MATRIZ        
class CourseGrid(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course)
    date_init = models.DateField()
    date_term = models.DateField()
    situation = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Grade Curricular"
            
        
#DISCIPLINA
class Discipline(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    course_grid = models.ForeignKey(CourseGrid)
    ementa = models.TextField()
    course = models.ForeignKey(Course)
    block = models.IntegerField()
    #area = models.ForeignKey(KnowledgeArea)
    work_load = models.IntegerField()
    situation = models.BooleanField()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Discplina"    
#TIPO-DE-CONTRATO
class ContractType(models.Model):
    name = models.CharField(max_length=50)
    wl_teaching = models.IntegerField()
    wl_extres = models.IntegerField()
    situation = models.BooleanField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Tipo de Contrato"
#PROFESSOR
class Teacher(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course)
    contract = models.ForeignKey(ContractType)
    #area = models.ForeignKey(KnowledgeArea)
    email = models.EmailField()
    phone1 = models.CharField(max_length=15)
    phone1 = models.CharField(max_length=15)
    contract_term = models.TextField()
    effective = models.BooleanField()
    situation = models.BooleanField()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Professores"



#TIPO-DE-ATIVIDADE
class ActivityType(models.Model):
    name = models.CharField(max_length=50)
    wl_week = models.IntegerField()
    wl_max = models.IntegerField()
    Type = models.IntegerField()
    situation = models.BooleanField()
    
    def __unicode__(self):
        return self.name
        
#ATIVIDADE        
class Actvity(models.Model):
    teacher = models.ForeignKey(Teacher)
    actv_type = models.ForeignKey(ActivityType)
    quantity = models.IntegerField()
    date_ini = models.DateField()
    date_term = models.DateField()
    comment = models.TextField()
    
    def __unicode__(self):
        return self.comment




