from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 4


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]



# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarMake, CarMakeAdmin)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
