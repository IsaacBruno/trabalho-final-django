from django.contrib import admin
from docentes.models import *
'''
class ContratoAdmin(admin.ModelAdmin):
    list_display=('descricao','ch','situacao')
    #search_fields=('')
    #ordering=('')
    #fields=('')
admin.site.register(contrato,ContratoAdmin)




class DisciplinaAdmin(admin.ModelAdmin):
    search_fields=('nome','curso')
    list_display=('nome','curso','bloco','ch','ementa','situacao')
    list_per_page=2
admin.site.register(disciplina,DisciplinaAdmin)


class EncargoAdmin(admin.ModelAdmin):
    list_display=('disciplina','professor','periodo')
admin.site.register(encargo,EncargoAdmin)'''

class CampusAdmin(admin.ModelAdmin):
    list_display=('name','situation')
admin.site.register(Campus,CampusAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=('name','campus','situation')
admin.site.register(Course,CourseAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','course','contract','email','phone1','situation')
admin.site.register(Teacher,TeacherAdmin)


class CourseGridAdmin(admin.ModelAdmin):
    list_display=('name','course','situation')
admin.site.register(CourseGrid, CourseGridAdmin)  


class DisciplineAdmin(admin.ModelAdmin):
    list_display=('name','course','situation')
admin.site.register(Discipline, DisciplineAdmin) 


class ContractTypeAdmin(admin.ModelAdmin):
    list_display=('name','situation')
    #search_fields=('')
    #ordering=('')
    #fields=('')
admin.site.register(ContractType,ContractTypeAdmin)     

