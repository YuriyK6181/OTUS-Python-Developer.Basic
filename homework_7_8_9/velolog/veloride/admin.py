from django.contrib import admin
from .models import Bike, BikeClass, BikeType, BikeEventType, Organization

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = "pk", "manufacturer", "model_name", "model_year", "description", "archived"
    list_display_links = "pk", "model_name"
    ordering = "model_year", "manufacturer", "model_name", "pk"


@admin.register(BikeClass)
class BikeClassAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "archived"
    list_display_links = "name", "pk"
    ordering =  "name", "pk"


@admin.register(BikeType)
class BikeTypeAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "archived"
    list_display_links = "name", "pk"
    ordering =  "name", "pk"


@admin.register(BikeEventType)
class BikeEventAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "archived"
    list_display_links = "name", "pk"
    ordering =  "name", "pk"

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "address", "org_email", "org_site", "phone1", "phone2"
    list_display_links = "pk", "name"
    ordering = "name", "pk"