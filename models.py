from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import re

# Create your models here.

class Tag(models.Model):
	"""
	Blog Topic Tags
	"""
	user = models.ForeignKey(User)
	name = models.CharField(max_length=32)
	slug = models.SlugField(max_length=128)
	
	def __unicode__(self):
		return self.name

	class Meta:
		pass

class Entry(models.Model):
	"""
	Individual Blog Entry model
	"""
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128)
	tags = models.ManyToManyField(Tag)
	pub_date = models.DateField(auto_now_add=True)
	body = models.TextField()

	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ('-pub_date',)
