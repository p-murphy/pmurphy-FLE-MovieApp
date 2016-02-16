from django.contrib import admin
from starter.models import Actor, Movie

class ChoiceInLine(admin.TabularInline):
	model = Actor
	extra = 5

class MovieAdmin(admin.ModelAdmin):
	inlines = [ChoiceInLine]

admin.site.register(Movie, MovieAdmin)

# Register your models here.
