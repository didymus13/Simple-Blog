# -*- coding: utf-8 -*-
# Create your views here.
from blog.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext




def entry_list (request, tag_slug=None, user=None):
    try:
        if tag_slug:
            e_list = Tag.objects.get(slug=tag_slug).entry_set.all()
        elif user:
            e_list = User.objects.get(username=user).entry_set.all()
        else:
            e_list = Entry.objects.all()
    except:
            e_list = Entry.objects.none()
    return render_to_response('blog/entry_list.html', {'e_list': e_list,})

def entry (request, slug):
    e = Entry.objects.get(slug__exact=slug)
    return render_to_response('blog/entry_detail.html', {
		'e' : e},
		context_instance=RequestContext(request), )

def get_comment_list(request, slug):
	e = Entry.objects.get(slug__exact=slug)
	return render_to_response('blog/comment_list.html', {'e': e,} )


@login_required
def entry_form (request, f_data=None, id=None):
	"""
	===========
	Pseudocode:
	===========
	if user has permission to post or edit entry
	if editing existing entry, make a form instance of object
	present entry form
	validate form on submission
	save form as new object
	display new entry
	"""
	pass

@login_required
def entry_delete (request, id=None):
	"""
	==========
	Pseudocode
	==========
	if user has permission to delete, 
	confirm intentions
	then delete
	"""
	pass
