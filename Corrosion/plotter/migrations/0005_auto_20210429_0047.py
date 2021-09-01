# Generated by Django 3.2 on 2021-04-29 00:47

from django.db import migrations, models
import plotter.models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0004_dropimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropimage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dropimage',
            name='image',
            field=models.ImageField(upload_to=plotter.models.drop_upload_dir),
        ),
    ]