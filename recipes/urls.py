from django.urls import path

from .views import(
    recipe_list_view,
    recipe_detail_view,
    recipe_delete_view,
    recipe_ingredient_delete_view,
    recipe_create_view,
    recipe_update_view,
    recipe_detail_htmx_view,
    recipe_ingredient_update_htmx_view,
    recipe_ingredient_image_upload_view
)

app_name = 'recipes'
urlpatterns = [
    path('', recipe_list_view, name='list'),
    path('create/', recipe_create_view, name='create'),
    path('<int:id>/edit/', recipe_update_view, name='update'),
    path('<int:id>/', recipe_detail_view, name='detail'),
    path('<int:id>/delete/', recipe_delete_view, name='delete'),
    path('<int:parent_id>/ingredient/<int:id>/delete/', recipe_ingredient_delete_view, name='ingredient-delete'),
    path('<int:parent_id>/image-upload/', recipe_ingredient_image_upload_view),# name='image-upload'),

    path('hx/<int:id>/', recipe_detail_htmx_view, name='htmx-detail'),
    path('hx/<int:parent_id>/ingredient/<int:id>/', recipe_ingredient_update_htmx_view, name='htmx-ingredient-detail'),
    path('hx/<int:parent_id>/ingredient/', recipe_ingredient_update_htmx_view, name='htmx-ingredient-create')
]


