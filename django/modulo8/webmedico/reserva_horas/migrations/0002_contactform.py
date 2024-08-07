# Generated by Django 4.2 on 2024-06-14 23:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reserva_horas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ontact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_name', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
    ]
