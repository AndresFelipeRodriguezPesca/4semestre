from django.contrib import admin
from characters.models import Character, Universe
# Register your models here.

admin.site.register(Character)

class Character(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')


admin.site.register(Universe)


class Universe(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
