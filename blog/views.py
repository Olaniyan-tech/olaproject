from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def blog_home_view(request, slug=None):
    blog_obj = None
    if slug is not None:
        try:
            blog_obj = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise Http404  #("Blog post not found.")
        except Blog.MultipleObjectsReturned:
             blog_obj = Blog.objects.get(slug=slug)   # blog_obj = Blog.objects.get(slug=slug).first()
        except:
            raise Http404 #("Something went wrong.")
    
    context = {
        'blog_obj' : blog_obj
    }
    return render(request, "blog/blog_detail.html", context)

def blog_search_view(request):
    query = request.GET.get('q')
    qs = Blog.objects.search(query=query)
        
    context = {'blog_list' : qs}
    return render(request, "blog/search.html", context)


@login_required
def create_blog(request):
    form = BlogForm(request.POST or None)
    context = {'form' : form}
    if form.is_valid():
        blog_obj = form.save()
        context['form'] = BlogForm()

        #return redirect("blog-details", slug=blog_obj.slug)
        return redirect(blog_obj.get_absolute_url())
       
    return render(request, "blog/create.html", context)