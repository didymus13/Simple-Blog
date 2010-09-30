from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm 
import re
from django.template.defaultfilters import slugify
# Create your models here.

class Tag(models.Model):
    """
    Tags to apply to a blog entry
    """
    label = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __unicode__(self):
        return self.label

    def get_absolute_url(self):
        return '/blog/tags/%s/' % self.slug

    def save(self, *args, **kwargs):
        if self.label and not self.slug:
            self.slug = slugify(self.label)
        super(Tag, self).save(*args, **kwargs)

	class Meta:
		ordering = ('label',)

class TagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ('label',)

class Entry(models.Model):
    """
    Individual Blog Entry model
    """
    user = models.ForeignKey(User )
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title
	
    def get_absolute_url(self):
        return '/blog/%s/' % self.slug

    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ('-pub_date',)
		
class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ('title', 'body', 'tags')
