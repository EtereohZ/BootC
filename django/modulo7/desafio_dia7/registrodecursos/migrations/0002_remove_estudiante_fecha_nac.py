# Generated by Django 4.2 on 2024-05-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrodecursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha_nac',
        ),
    ]