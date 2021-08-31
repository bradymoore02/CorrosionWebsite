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

class Technique(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    detailed_description = models.CharField(max_length=10000)
    def get_absolute_url(self):
        return reverse('plotter-technique-detail', args=[str(self.id)])

class Test(models.Model):

    date = models.DateTimeField()
    substrate = models.ForeignKey(Substrate, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.date.strftime('%m/%d/%Y'))
