# Generated by Django 3.2.5 on 2021-09-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0012_remove_sample_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='composition',
            field=models.JSONField(default={'iron': '.01', 'nickel': '.99'}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='yield_strength',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]