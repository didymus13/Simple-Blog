from django.conf.urls.defaults import *
from blog.models import Entry
from blog.views import LatestBlogEntriesFeed
'''
Blog URLs should be the following
	/blog/					: get list of all
	/blog/SLUGID			: show specific blog entry
	/blog/page/1    		: blog list with pagination
	/blog/new				: creates a new entry
	/blog/rss				: rss blog 
	/blog/slug/edit			: edits the entry
	/blog/slug/delete		: deletes the entry
	/blog/tags				: list all available tags
	/blog/tags/tag			: lists all blog posts with that tag
	/blog/tags/new			: create a new tag
	/blog/tags/tag/edit		: edit an existing tag
	/blog/tags/tag/delete	: deletes the tag
'''

urlpatterns = patterns('blog.views',
    (r'^$', 'entry_list'),
    (r'^page/(?P<page>\d+)/$', 'entry_list'),
    (r'^new/$', 'entry_form' ),
    (r'^rss/$', LatestBlogEntriesFeed() ),
	(r'^tags/$', 'tag_list'),
	(r'^tags/new/$', 'tag_form'),
	(r'^tags/(?P<tag>[-\w]+)/$', 'entry_list'),
	(r'^tags/(?P<tag>[-\w]+)/edit/$', 'tag_form'),
	(r'^tags/(?P<tag>[-\w]+)/delete/$', 'tag_delete'),
    (r'^(?P<slug>[-\w]+)/$', 'entry' ),
    (r'^(?P<slug>[-\w]+)/edit/$', 'entry_form' ),
    (r'^(?P<slug>[-\w]+)/delete/$', 'entry_delete' ),
    
	## Example:
	##(r'^$', 'date_based.archive_index', dict(blog_dict, template_name='blog/entry_list.html', template_object_name='entry' )),
	#(r'^(?P<year>\d+)/$', 'date_based.archive_year', dict(blog_dict, make_object_list=True, date_field= 'pub_date',)),
	#(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'date_based.archive_month', dict(blog_dict, month_format="%m", date_field= 'pub_date',)),
	#(r'^\d+/\d+/(?P<slug>[-\w]+)/$', 'list_detail.object_detail', dict(blog_dict, template_name='blog/entry_detail.html',)),
	##(r'^/tag/(?P<tag>)/$', 'list_detail.object_list', dict(blog_dict, 
)


#piston API resources
from piston.resource import Resource
from blog.handlers import *

blog_entry_handler = Resource(EntryHandler)
blog_tag_handler = Resource(TagHandler)

urlpatterns += patterns('',
    (r'^api/entry/$', blog_entry_handler),
    (r'^api/entry/(?P<slug>[-\w]+)/$', blog_entry_handler),
    (r'^api/tag/$', blog_tag_handler),
    (r'^api/tag/(?P<tag>[-\w]+)/$', blog_tag_handler),
)
