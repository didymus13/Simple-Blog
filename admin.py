from blog.models import *
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",) }

admin.site.register(Entry, EntryAdmin )
