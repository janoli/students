from django.contrib import admin
from .models import Alumno, Curso, CicloLectivo, Ficha, Nota, Talones_de_pago, Valor_cuota

# Register your models here.
 

class FichaInline(admin.StackedInline):
    model = Ficha
    extra = 0

class NotaInline(admin.StackedInline):
    model = Nota
    extra = 0

class Talones_de_pagoInline(admin.StackedInline):
    model = Talones_de_pago
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
    list_display =  ('alumno', 'año_de_cursado', 'curso')
    #search_fields = ['apellido']

    inlines = [NotaInline, Talones_de_pagoInline]
    list_filter = ['año_de_cursado', 'curso']

class PagoAdmin(admin.ModelAdmin):
    fields = ['ficha', 'fecha']
    list_display =  ('ficha','fecha')
    #list_filter = ['año']

class NotaAdmin(admin.ModelAdmin):
    #fields = ['apellido', 'nombre', 'dni', 'pub_date']
    list_display =  ('ficha', 'trimestre')
    #search_fields = ['apellido', 'dni']

    list_filter = ['trimestre']



admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CicloLectivo, CicloLectivoAdmin)
admin.site.register(Curso)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(Talones_de_pago)
admin.site.register(Valor_cuota)

#admin.site.register(CicloLectivoAdmin)
