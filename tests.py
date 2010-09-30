import unittest, re
from blog.models import *
from django.contrib.auth.models import *
from django.db import IntegrityError
from django.test.client import Client

class TagTestCase(unittest.TestCase):
    def testNewTagShouldBeEmpty(self):
        t = Tag()
        self.assertEquals('', t.label)
        self.assertEquals('', t.slug)

    def testNewTagWithoutSlugShouldGetOne(self):
        t = Tag(label='test')
        t.save()
        self.assertEquals('test', t.slug)  
        t.delete()      

class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self.u = User(username='tester', password='12345')
        self.u.save()
        self.t1 = Tag(label='test')
        self.t1.save()
        self.t2 = Tag(label='another test')
        self.t2.save()

    def tearDown(self):
        self.u.delete()
        self.t1.delete()
        self.t2.delete()

    def testNewEntryWithoutSlugShouldGetOne(self):
        e = Entry(title='test title', user=self.u)
        e.save()
        self.assertEquals('test-title', e.slug)

    def testEntryCanAcceptMultipleTags(self):
        e = Entry(title='test entry', user=self.u)
        e.save()
        e.tags.add(self.t1)
        e.tags.add(self.t2)
        e.save()

        self.assertEquals('test entry', e.title)
        self.assertEquals(2, e.tags.all().count())

        e.delete()

    def testListEntriesByTag(self):
        e = Entry(user=self.u, title='Test Live Entry')
        e.save()
        e.tags.add(self.t1)
        e.save()

        self.assertEquals(1, Entry.objects.all().count() )
        self.assertEquals(1, Entry.objects.filter(tags__slug=self.t1.slug).count())
        self.assertEquals(0, Entry.objects.filter(tags__slug=self.t2.slug).count())

        c = Client()
        test_response = c.get('/blog/tags/test/')
        self.assertNotEquals(None, re.search('Test Live Entry', test_response.content))

        another_response = c.get('/blog/tags/another-test/')
        self.assertEquals(None, re.search('Test Live Entry', another_response.content))

        e.delete()
        
