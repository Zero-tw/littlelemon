from django.contrib import admin

from restaurant import models

# Register your models here.
admin.site.register(models.Menu)
admin.site.register(models.Booking)