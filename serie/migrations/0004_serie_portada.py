# Generated by Django 4.2.5 on 2023-10-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("serie", "0003_serie_sinopsis"),
    ]

    operations = [
        migrations.AddField(
            model_name="serie",
            name="portada",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]