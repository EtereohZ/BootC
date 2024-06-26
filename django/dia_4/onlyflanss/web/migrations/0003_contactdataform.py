# Generated by Django 3.2.4 on 2024-05-13 20:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20240513_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDataForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customer_email', models.EmailField(max_length=254)),
                ('cutomer_name', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
    ]
