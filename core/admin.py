from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.CTE)
admin.site.register(models.CTE_product)
admin.site.register(models.Contract)
admin.site.register(models.ContractCTE)