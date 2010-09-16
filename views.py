# -*- coding: utf-8 -*-
# Create your views here.
from blog.models import *
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.contrib.syndication.views import Feed

class LatestBlogEntriesFeed(Feed):
    title = "StephaneDoiron.com site news"
    link = "/blog/"
    description = "Updates on StephaneDoiron.com"

    def items(self):
        return Entry.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body


def entry_list (request, page=1):
    try:
        e_list = Entry.objects.all()
    except:
        e_list = Entry.objects.none()
    p = Paginator(e_list, 10)
    try:
        entries = p.page(page)
    except (EmptyPage, InvalidPage):
        entries = p.page(p.num_pages)
    return render_to_response('blog/entry_list.html', {'e_list': entries,})

def entry (request, slug):
    e = Entry.objects.get(slug__exact=slug)
    return render_to_response('blog/entry_detail.html', {
		'pageTitle': e.title,
        'e' : e},
		context_instance=RequestContext(request), )

@login_required
def entry_form (request, slug=None):
    if slug:
        e = get_object_or_404(Entry, slug=slug)
    else:
        e = Entry()
    
    if request.method == 'POST':
        print 'POST submitted'
        
        if id:
            f = EntryForm(request.POST, instance=e);
        else:
            f = EntryForm(request.POST)
        
        print f
        
        if f.is_valid():
            print 'valid form'
            e = f.save(commit=False)
            e.slug = slugify(e.title)
            e.user = request.user
            e.save()
            return redirect(e)
    
    f = EntryForm(instance=e)
    return render_to_response('blog/entry_form.html', 
        {'f': f, 'pageTitle': "Blog entry form"} , 
        context_instance=RequestContext(request) )
        
    

@login_required
def entry_delete (request, slug=None):
    e = get_object_or_404(Entry, slug=slug)
    e.delete()
    return redirect('/blog')
