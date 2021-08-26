from django.db import models
from django.urls import reverse
from django.conf import settings
import os


def drop_upload_dir(instance, filename):
    return 'images/drops/{}/{}'.format(instance.drop.id, filename)


class Substrate(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Test(models.Model):

    date = models.DateTimeField()
    substrate = models.ForeignKey(Substrate, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.date.strftime('%m/%d/%Y'))


class Drop(models.Model):

    number = models.IntegerField()
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    stage_temp = models.FloatField()
    tip_temp = models.FloatField()
    contact_angle = models.FloatField()

    def save(self, *args, **kwargs):
        super(Drop, self).save(*args, **kwargs)
        os.mkdir(os.path.join(settings.MEDIA_ROOT, str(self.id)))

    def __str__(self):
        return 'Drop {} on {}'.format(self.number, self.test)

    def get_absolute_url(self):
        return reverse('plotter-drop-detail', args=[str(self.id)])


class DropImage(models.Model):

    choices = [
        ('Cropped', 'Cropped'),
        ('Fitted', 'Fitted'),
        ('Full', 'Full'),
        ('Other', 'Other'),
    ]

    drop = models.ForeignKey(Drop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=drop_upload_dir)
    description = models.TextField(null=True)
    image_type = models.CharField(max_length=20,
                                  choices=choices,
                                  default='Other')

    def __str__(self):
        return 'Image of drop {} on {}'.format(self.drop.number,
                                               str(self.drop.test.date.date()))
