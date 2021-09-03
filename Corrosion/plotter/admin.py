from django.contrib import admin
from .models import Technique, Material, Sample, MaterialType

admin.site.register(Technique)
admin.site.register(Material)
admin.site.register(MaterialType)
admin.site.register(Sample)
