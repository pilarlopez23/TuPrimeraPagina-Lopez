# Generated by Django 4.2.5 on 2023-10-14 17:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inicio", "0002_pelicula_sinopsis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pelicula",
            name="sinopsis",
            field=ckeditor.fields.RichTextField(),
        ),
    ]