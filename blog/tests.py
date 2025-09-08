from django.test import TestCase
# Create your tests here.
from django.utils.text import slugify
from .models import Blog, BlogQuerySet
from .utils import slugify_instance_title 

class BlogTestCase(TestCase):
    def setUp(self):
        self.number_of_blog = 20
        for _ in range(0, self.number_of_blog):
            Blog.objects.create(title='Bro, just cool', content='Oya oya')

    def test_queryset_exists(self):
        qs = Blog.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Blog.objects.all()
        self.assertEqual(qs.count(), self.number_of_blog)
    
    def test_bro_just_cool_slug(self):
        obj = Blog.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)

    def test_bro_just_cool_uniqueslug(self):
        qs = Blog.objects.exclude(slug__iexact='bro-just-cool')

        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug, slugified_title)  

    def test_slugify_instance_title(self):
        obj = Blog.objects.all().last()
        new_slug = []

        for _ in range(0, 30):
            instance = slugify_instance_title(obj, save=True)
            new_slug.append(instance.slug)
        
        unique_slugs = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slugs))  
    
    def test_slugify_instance_title_2(self):
        slug_list = Blog.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))
    
    def test_added_user_slug_unique(self):
        base_title = 'Bro, just cool'
        slugs = []

        for _ in range(0, 30):
            obj = Blog.objects.create(title=base_title, content='Okayyy, O wise')
            instance = slugify_instance_title(obj, save=True)
            slugs.append(instance.slug)
        
        unique_slugs = set(slugs)
        self.assertEqual(len(slugs), len(unique_slugs))
    
    def test_blog_search_manager(self):
        qs = Blog.objects.search(query="Bro, just cool")
        self.assertEqual(qs.count(), self.number_of_blog)
        qs = Blog.objects.search(query="Bro, just cool")
        self.assertEqual(qs.count(), self.number_of_blog)
        qs = Blog.objects.search(query="Oya oya")
        self.assertEqual(qs.count(), self.number_of_blog)


