# Generated by Django 4.0.5 on 2022-08-08 20:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]