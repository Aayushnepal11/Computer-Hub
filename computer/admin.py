from django.contrib import admin
from .models import ComputerBarnd, ComputerSpecification, Computer
# Register your models here.

admin.site.register(ComputerBarnd)
admin.site.register(ComputerSpecification)
admin.site.register(Computer)
