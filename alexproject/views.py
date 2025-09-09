"""
To render html pages
"""


from django.http import HttpResponse
from blog.models import Blog
from django.template.loader import render_to_string

import random

def home(request, *args, **kwargs):
    """
    Django sent us a request, take in the request
    and return the response in form of HTML
    """
    print(args, kwargs)

    obj_list = Blog.objects.all()

    blog_obj = None
    blog_title = ""
    blog_content = ""

    if obj_list.exists():
        blog_obj = random.choice(obj_list)
        blog_title = blog_obj.title
        blog_content = blog_obj.content

    
    context = {"obj_list" : obj_list,
               "title" : blog_title,
               "content" : blog_content,
               "id" : blog_obj.id if blog_obj else None
               }


    HTML_STRING = render_to_string('home.html', context)
    return HttpResponse(HTML_STRING)



