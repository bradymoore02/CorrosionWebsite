# Generated by Django 3.2.5 on 2021-08-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0008_auto_20210831_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='url',
            field=models.CharField(default='http://localhost:8000/admin/plotter/technique/add/', max_length=100),
            preserve_default=False,
        ),
    ]
