from blog.models import *
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",) }

admin.site.register(Entry, EntryAdmin )

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("label",) }

admin.site.register(Tag, TagAdmin )
