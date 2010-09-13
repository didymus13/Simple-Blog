from django.conf.urls.defaults import *
from blog.models import Entry, Tag

'''
Blog URLs should be the following
 * /blog/		: get list of all
 * /blog/user/USERID	: get list of all entries for that user
 * /blog/tag/TAGID	: get list of all with tag
 * /blog/SLUGID		: show specific blog entry
 * /blog/new		: creates a new entry
 * /blog/ID/edit	: edits the entry
 * /blog/ID/delete	: deletes the entry
 * /blog/date/YEAR	: lists all entries for that year
 * /blog/date/YEAR/MONTH : lists all entries for that year/month
'''

urlpatterns = patterns('blog.views',
    (r'^$', 'entry_list'),
    (r'^new/$', 'entry_form' ),
    (r'^(?P<slug>[-\w]+)/$', 'entry' ),
    (r'^(?P<slug>[-\w]+)/edit/$', 'entry_form' ),
    (r'^tag/(?P<tag_slug>[-\w]+)/$', 'entry_list'),
    
	## Example:
	##(r'^$', 'date_based.archive_index', dict(blog_dict, template_name='blog/entry_list.html', template_object_name='entry' )),
	#(r'^(?P<year>\d+)/$', 'date_based.archive_year', dict(blog_dict, make_object_list=True, date_field= 'pub_date',)),
	#(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'date_based.archive_month', dict(blog_dict, month_format="%m", date_field= 'pub_date',)),
	#(r'^\d+/\d+/(?P<slug>[-\w]+)/$', 'list_detail.object_detail', dict(blog_dict, template_name='blog/entry_detail.html',)),
	##(r'^/tag/(?P<tag>)/$', 'list_detail.object_list', dict(blog_dict, 
)
