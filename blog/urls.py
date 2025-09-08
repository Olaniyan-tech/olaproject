
from django.urls import include, path

from blog.views import(
    blog_search_view,
    create_blog,
    blog_home_view
)

app_name = 'blog'
urlpatterns = [
    path('', blog_search_view, name='search'),
    path('create_blog/', create_blog, name='create'),
    path('<slug:slug>/', blog_home_view, name='details'),
]
