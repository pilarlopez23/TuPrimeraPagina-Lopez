# Generated by Django 4.2.5 on 2023-11-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cuentas", "0002_rename_infoadicional_infoextra"),
    ]

    operations = [
        migrations.AddField(
            model_name="infoextra",
            name="pais",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
