from django.conf.urls.defaults import *
from blog.models import Entry

'''
Blog URLs should be the following
 * /blog/		: get list of all
 * /blog/SLUGID		: show specific blog entry
 * /blog/page/1     : blog list with pagination
 * /blog/new		: creates a new entry
 * /blog/slug/edit	: edits the entry
 * /blog/slug/delete	: deletes the entry
'''

urlpatterns = patterns('blog.views',
    (r'^$', 'entry_list'),
    (r'^page/(?P<page>\d+)/$', 'entry_list'),
    (r'^new/$', 'entry_form' ),
    (r'^(?P<slug>[-\w]+)/$', 'entry' ),
    (r'^(?P<slug>[-\w]+)/edit/$', 'entry_form' ),
    (r'^(?P<slug>[-\w]+)/delete/$', 'entry_delete' ),
 #   (r'^tag/(?P<tag_slug>[-\w]+)/$', 'entry_list'),
    
	## Example:
	##(r'^$', 'date_based.archive_index', dict(blog_dict, template_name='blog/entry_list.html', template_object_name='entry' )),
	#(r'^(?P<year>\d+)/$', 'date_based.archive_year', dict(blog_dict, make_object_list=True, date_field= 'pub_date',)),
	#(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'date_based.archive_month', dict(blog_dict, month_format="%m", date_field= 'pub_date',)),
	#(r'^\d+/\d+/(?P<slug>[-\w]+)/$', 'list_detail.object_detail', dict(blog_dict, template_name='blog/entry_detail.html',)),
	##(r'^/tag/(?P<tag>)/$', 'list_detail.object_list', dict(blog_dict, 
)
