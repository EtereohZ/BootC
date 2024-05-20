# Generated by Django 3.2.4 on 2024-05-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField()),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('img_url', models.URLField()),
                ('slug', models.SlugField()),
                ('is_private', models.BooleanField()),
            ],
        ),
    ]