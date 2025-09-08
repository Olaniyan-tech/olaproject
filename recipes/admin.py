from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredients, RecipeIngredientsImage

admin.site.register(RecipeIngredientsImage)


admin.site.register(RecipeIngredients)

class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    #fields = ['name', 'quantity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]
    list_display = ['user', 'name']
    readonly_fields = ['created', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin) 


