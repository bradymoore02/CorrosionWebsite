# Generated by Django 3.2.5 on 2021-08-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0007_alter_dropimage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='dropimage',
            name='drop',
        ),
        migrations.DeleteModel(
            name='Drop',
        ),
        migrations.DeleteModel(
            name='DropImage',
        ),
    ]
