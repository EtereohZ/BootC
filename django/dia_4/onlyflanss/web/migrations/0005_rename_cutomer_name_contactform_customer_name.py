# Generated by Django 3.2.4 on 2024-05-13 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_contactdataform_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='cutomer_name',
            new_name='customer_name',
        ),
    ]