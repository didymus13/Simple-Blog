from piston.handler import AnonymousBaseHandler, BaseHandler
from piston.utils import rc, validate
from blog.models import *
from django.shortcuts import redirect, get_object_or_404

class AnonymousEntryHandler(AnonymousBaseHandler):
    allowed_methods = ('GET',)
    model = Entry

class EntryHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Entry
    anonymous = AnonymousEntryHandler

    def read(self, request, slug=None):
        entries = Entry.objects
        if slug:
            return entries.get(slug=slug)
        else:
            return entries.all()


class AnonymousTagHandler(AnonymousBaseHandler):
    allowed_methods = ('GET',)
    model = Tag

class TagHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Tag
    anonymous = AnonymousTagHandler

    def read(self, request, tag=None):
        """
        If a tag is given, return all entries with that tag. Else return list of 
        tags.
        @param string tag
        """
        tags = Tag.objects
        if tag:
            t = tags.get(slug=tag)
            return t.entry_set.all()
        else:
            return tags.all()

    def update(self, request, tag):
        t = get_object_or_404(Tag, slug=tag)
        f = TagForm(request.PUT, instance=t)
        return f.save()

    def create(self, request):
        f = TagForm(request.POST)
        return f.save()        

    def delete(self, request, tag):
        t = get_object_or_404(Tag, slug=tag)
        t.delete()        
        return rc.DELETED
