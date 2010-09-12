from blog.models import *
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",) }

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",) }

admin.site.register(Entry, EntryAdmin )
admin.site.register(Tag, TagAdmin )
