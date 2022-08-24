from django.contrib import admin
from .models import House, HouseImage

# Register your models here.

class HouseImageAdmin(admin.StackedInline):
	model = HouseImage

@admin.register(House)

class HouseAdmin(admin.ModelAdmin):
	inlines = [HouseImageAdmin]

	class Meta:
		model = House

@admin.register(HouseImage)

class HouseImageAdmin(admin.ModelAdmin):
	pass
