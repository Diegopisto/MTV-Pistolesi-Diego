# Generated by Django 4.0.6 on 2022-07-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiamtv', '0002_remove_familia_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='fecha_nacimiento',
            field=models.DateField(null=True, unique=True),
        ),
    ]
