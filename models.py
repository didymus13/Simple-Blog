from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm 
import re
# Create your models here.

class Entry(models.Model):
	"""
	Individual Blog Entry model
	"""
	user = models.ForeignKey(User )
	title = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128)
	pub_date = models.DateField(auto_now_add=True)
	body = models.TextField()

	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return '/blog/%s' % self.slug
	
	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ('-pub_date',)
		
class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ('title', 'body',  )
