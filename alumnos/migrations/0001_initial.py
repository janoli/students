# Generated by Django 3.2.12 on 2022-09-05 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=11)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='CicloLectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.CharField(max_length=4)),
                ('fecha_ini', models.DateField(verbose_name='Inicio Ciclo Lectivo')),
                ('fecha_fin', models.DateField(verbose_name='Fin Ciclo Lectivo')),
            ],
            options={
                'verbose_name_plural': 'Ciclo Lectivo',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_text', models.CharField(max_length=80)),
                ('cicloLectivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.ciclolectivo', verbose_name='Ciclo Lectivo')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año_de_cursado', models.CharField(max_length=4)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.ficha')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.CharField(choices=[('1', '1º TRIMESTRE'), ('2', '2º TRIMESTRE'), ('3', '3º TRIMESTRE'), ('4', '4º TRIMESTRE')], default='1º Trimestre', max_length=1)),
                ('examen_bimestral', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('concepto', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ejercitacion_oral', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ejercitación Oral')),
                ('ejercitacion_escrita', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ejercitación Escrita')),
                ('literatura', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.ficha')),
            ],
            options={
                'ordering': ['trimestre'],
            },
        ),
    ]
