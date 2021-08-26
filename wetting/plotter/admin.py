from django.contrib import admin
from .models import Substrate, Test, Drop, DropImage

admin.site.register(Substrate)
admin.site.register(Test)
admin.site.register(Drop)
admin.site.register(DropImage)
