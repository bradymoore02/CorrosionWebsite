from django.db import models
from django.urls import reverse
from django.conf import settings
import os

def drop_upload_dir(instance, filename):
    return 'images/drops/{}/{}'.format(instance.drop.id, filename)

def sample_upload_dir(instance, filename):
    return 'images/samples/{}/{}'.format(instance.sample.id, filename)

def technique_upload_dir(instance, filename):
    return 'images/techniques/{}/{}'.format(instance.technique.id, filename)


class Technique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    detailed_description = models.TextField()
    def get_absolute_url(self):
        return reverse('technique-detail', args=[str(self.id)])
    def __str__(self):
        return self.name

class MaterialType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    detailed_description = models.TextField()
    type = models.ForeignKey(MaterialType, on_delete=models.PROTECT)
    composition = models.JSONField()
    yield_strength = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('material-detail', args=[str(self.id)])
    def __str__(self):
        return self.name


class Sample(models.Model):
    number = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    roughness = models.CharField(max_length=100)
    mass_before = models.CharField(max_length=100)
    mass_after = models.CharField(max_length=100)
    def __str__(self):
        return "Sample " + str(self.number)

    def get_absolute_url(self):
        return reverse('sample-detail', args=[str(self.id)])


class SampleImage(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=sample_upload_dir)
    def __str__(self):
        return self.sample.name

class TechniqueImage(models.Model):
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=technique_upload_dir)
    def __str__(self):
        return self.technique.name
