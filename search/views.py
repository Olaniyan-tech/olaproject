from django.shortcuts import render

from blog.models import Blog
from recipes.models import Recipe
# Create your views here.

SEARCH_TYPE_MAPPING = {
    'blog' : Blog,
    'blog' : Blog,
    'recipe' : Recipe,
    'recipes' : Recipe
}

def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    Klass = Recipe
    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.objects.search(query=query)
    context = {'queryset' : qs}
    templates = "search/result-view.html"
    if request.htmx:
        context['queryset'] = qs[:5]
        templates = "search/partials/results.html"
    return render(request, templates, context)
 