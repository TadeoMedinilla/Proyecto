# Generated by Django 4.0.5 on 2022-07-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebF1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativo',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='administrativo',
            name='exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empleado',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ingeniero',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='ingeniero',
            name='exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='periodista',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='periodista',
            name='matricula',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='piloto',
            name='camp_disp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='piloto',
            name='camp_gan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='piloto',
            name='exp',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='team',
            name='cant_emp',
            field=models.IntegerField(default=0),
        ),
    ]
