# Generated by Django 4.0.5 on 2022-08-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebF1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('descripcion', models.CharField(default='', max_length=500)),
            ],
        ),
    ]