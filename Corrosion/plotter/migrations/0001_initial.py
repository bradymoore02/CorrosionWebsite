# Generated by Django 3.2 on 2021-04-22 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Substrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('substrate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plotter.substrate')),
            ],
        ),
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('stage_temp', models.FloatField()),
                ('tip_temp', models.FloatField()),
                ('contact_angle', models.FloatField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plotter.test')),
            ],
        ),
    ]
