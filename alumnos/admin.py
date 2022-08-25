from django.contrib import admin
from .models import Alumno, Curso, CicloLectivo, Ficha, Notas

# Register your models here.
 

class FichaInline(admin.StackedInline):
    model = Ficha
    extra = 0

class NotasInline(admin.StackedInline):
    model = Notas
    extra = 0


class AlumnoAdmin(admin.ModelAdmin):
    #fields = ['apellido', 'nombre', 'dni', 'pub_date']
    list_display =  ('apellido', 'nombre', 'dni')
    search_fields = ['apellido', 'dni']

    inlines = [FichaInline]

class CicloLectivoAdmin(admin.ModelAdmin):
    #fields = ['ficha_alumno', 'curso']
    list_display =  ('año', 'fecha_ini', 'fecha_fin')
    list_filter = ['año']

class FichaAdmin(admin.ModelAdmin):
    #fields = ['apellido', 'nombre', 'dni', 'pub_date']
    #list_display =  ('apellido', 'nombre', 'dni')
    #search_fields = ['apellido']

    inlines = [NotasInline]
    list_filter = ['año_de_cursado', 'curso']


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CicloLectivo, CicloLectivoAdmin)
admin.site.register(Curso)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Notas)
#admin.site.register(CicloLectivoAdmin)
