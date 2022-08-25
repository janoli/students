from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime


# Create your models here.

class Alumno(models.Model):   
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=11)
    pub_date = models.DateTimeField('date published')
    email = models.EmailField()
    
    '''
    Dirección de correo electrónico
    Fecha de nacimiento
    Teléfono del trabajo
    Teléfono particular
    Dirección 
    Ciudad / Estado
    Provincia
    Código Postal
    País
    Inactivo
    Talle Remeras
    Covid-19
    Convenio

    '''

    def __str__(self):
        return self.apellido + ", " + self.nombre + " (" + self.dni + ")"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def nombre_completo(self):
        return self.apellido + ", " + self.nombre 

class CicloLectivo(models.Model):   
    año = models.CharField(max_length=4)
    fecha_ini = models.DateField('Inicio Ciclo Lectivo')
    fecha_fin = models.DateField('Fin Ciclo Lectivo')

    class Meta:
        #ordering = ["horn_length"]
        verbose_name_plural = "Ciclo Lectivo"

    def __str__(self):
        return self.año

class Curso(models.Model):
    curso_text = models.CharField(max_length=80)
    cicloLectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.curso_text + " - " + self.cicloLectivo.año

class Ficha(models.Model):
    año_de_cursado = models.CharField(max_length=4)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE )

    def __str__(self):
        return self.alumno.nombre_completo() + " - " + self.año_de_cursado

class Pago(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    fecha = models.DateField()
    primTrim = models.CharField(max_length=1)
    seguTrim = models.CharField(max_length=1)
    tercTrim = models.CharField(max_length=1)

    def __str__(self):
        return self.ficha.alumno.nombre_completo() + " - " + self.ficha.curso.curso_text


class Notas(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    primTrim = models.CharField(max_length=1)
    seguTrim = models.CharField(max_length=1)
    tercTrim = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "Notas"

    def __str__(self):
        return self.ficha.alumno.nombre_completo() + " - " + self.ficha.curso.curso_text