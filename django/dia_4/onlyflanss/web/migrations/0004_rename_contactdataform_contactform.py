# Generated by Django 3.2.4 on 2024-05-13 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactdataform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactDataForm',
            new_name='ContactForm',
        ),
    ]
