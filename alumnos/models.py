from audioop import avg
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
    cicloLectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE,
        verbose_name='Ciclo Lectivo')
    
    def __str__(self):
        return self.curso_text + " - " + self.cicloLectivo.año

class Ficha(models.Model):
    año_de_cursado = models.CharField(max_length=4)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE )

    def __str__(self):
        return self.alumno.nombre_completo() + " - " + self.año_de_cursado

    '''
    TODO: 
    1) Al inscribirse genera una ficha con todos los pagos futuros.  Como no se
    tiene un monto exacto de la cuota, se genera simplemente un registro de pago
    que deberá hacerse después, con el monto que tengan las cuotas.

    2) 
    '''        

class Pago(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return self.ficha.alumno.nombre_completo() + " - " + self.ficha.curso.curso_text


class Nota(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    
    PRIMERO = '1'
    SEGUNDO = '2'
    TERCERO = '3'
    CUARTO = '4'
    TRIMESTRE_CHOICES = [
        (PRIMERO, '1º TRIMESTRE'),
        (SEGUNDO, '2º TRIMESTRE'),
        (TERCERO, '3º TRIMESTRE'),
        (CUARTO, '4º TRIMESTRE'),
    ]
    trimestre = models.CharField(
        max_length=1,
        choices=TRIMESTRE_CHOICES,
        default="1º Trimestre",        
    )       

    examen_bimestral = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    concepto = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ejercitacion_oral = models.DecimalField(max_digits=4, decimal_places=2, blank=True, 
        null=True, verbose_name="Ejercitación Oral")
    ejercitacion_escrita = models.DecimalField(max_digits=4, decimal_places=2, blank=True, 
        null=True, verbose_name="Ejercitación Escrita")
    literatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    
    '''
        FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    '''

    # trimestre = OPTIONS
    # valor = decimalField
    # valor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
    #    verbose_name='Nota / Inasistencia')
    

    class Meta:
        ordering = ['trimestre']

    def __str__(self):
        return self.ficha.alumno.nombre_completo() + " - Ficha: " + self.ficha.año_de_cursado + " - " + self.txtTrimestre() + " TRIMESTRE"


    def txtTrimestre(self):
        if self.trimestre == "1":
            return "PRIMER"
        elif self.trimestre == "2":
            return "SEGUNDO "
        elif self.trimestre == "3":
            return "TERCER"
        elif self.trimestre == "4":
            return "CUARTO"

