from django.contrib import admin
from .models import Alumno, Curso, CicloLectivo, Inscripcion, Notas

# Register your models here.
 

class InscripcionInline(admin.StackedInline):
    model = Inscripcion
    extra = 3

class NotasInline(admin.StackedInline):
    model = Notas
    extra = 0


class AlumnoAdmin(admin.ModelAdmin):
    fields = ['apellido', 'nombre', 'dni', 'pub_date']
    list_display =  ('apellido', 'nombre', 'dni')
    search_fields = ['apellido']

    inlines = [InscripcionInline]

class CicloLectivoAdmin(admin.ModelAdmin):
    #fields = ['ficha_alumno', 'curso']
    list_display =  ('año', 'fecha_ini', 'fecha_fin')
    list_filter = ['año']

class InscripcionAdmin(admin.ModelAdmin):
    #fields = ['apellido', 'nombre', 'dni', 'pub_date']
    #list_display =  ('apellido', 'nombre', 'dni')
    #search_fields = ['apellido']

    inlines = [NotasInline]


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CicloLectivo, CicloLectivoAdmin)
admin.site.register(Curso)
#admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Notas)
#admin.site.register(CicloLectivoAdmin)
