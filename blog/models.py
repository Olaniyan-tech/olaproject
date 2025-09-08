from django.db import models
from django.conf import settings
from django.db.models import Q
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)
    
class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    objects = BlogManager()

    @property
    def name(self):
        return self.title
    
    def get_absolute_url(self):
        #return f'/blog/{self.slug}'
        return reverse('blog:details', kwargs={'slug' : self.slug})
    
    def save(self, *args, **kwargs):
        #if self.slug is None:
         #   self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        

def pre_save_blog(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(pre_save_blog, sender=Blog)


def post_save_blog(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(post_save_blog, sender=Blog)
