# Generated by Django 4.0.5 on 2022-08-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leido', models.BooleanField()),
                ('autor', models.CharField(default='', max_length=25)),
                ('destinatario', models.CharField(default='', max_length=25)),
                ('cuerpo', models.CharField(default='', max_length=500)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
