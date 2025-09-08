from django.contrib import admin

# Register your models here.
from blog.models import Blog

class AdminBlog(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['id', 'title', 'content']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Blog, AdminBlog)