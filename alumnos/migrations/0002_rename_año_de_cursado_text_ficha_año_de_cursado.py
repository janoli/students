# Generated by Django 4.0.6 on 2022-08-23 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficha',
            old_name='Año_de_cursado_text',
            new_name='año_de_cursado',
        ),
    ]
