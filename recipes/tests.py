from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Recipe, RecipeIngredients

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alli', password='alli1234')
    
    def test_user_password(self):
        check = self.user.check_password('alli1234')
        self.assertTrue(check)
    

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alli', password='alli1234')
        #self.user = User.objects.create_user(username='ayo', password='alli1234')
        self.recipe_a = Recipe.objects.create(user=self.user, name='Fried Rice')
        self.recipe_b = Recipe.objects.create(user=self.user, name='Jollof Rice')

        self.recipe_ingredient_a = RecipeIngredients.objects.create(
            recipe=self.recipe_a, 
            name='rice', 
            quantity='2', 
            unit='pounds')
        
        self.recipe_ingredient_b = RecipeIngredients.objects.create(
            recipe=self.recipe_a, 
            name='rice', 
            quantity='dqSREFDED', 
            unit='ounces')
    
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_reverse_count(self):
        user = self.user
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(), 2)
    
    def test_user_recipe_forward_count(self):
        user = self.user
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredients_set.all()
        self.assertEqual(qs.count(), 2)
    
    def test_user_recipe_ingredientcount(self):
        recipe = self.recipe_a  #Fried Rice
        qs = RecipeIngredients.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 2)
    
    def test_two_level_relation(self):
        user = self.user
        qs = RecipeIngredients.objects.filter(recipe__user = user)
        self.assertEqual(qs.count(), 2)
    
    def test_two_level_reverse_relation(self):
        user = self.user
        recipeIngredientids = list(user.recipe_set.all().values_list('recipeingredients__id', flat=True))
        qs = RecipeIngredients.objects.filter(id__in = recipeIngredientids)
        self.assertEqual(qs.count(), 2)

    def test_two_level_relation_via_recipe(self):
        user = self.user
        ids = user.recipe_set.all().values_list('id', flat=True)
        qs = RecipeIngredients.objects.filter(recipe__id__in = ids)
        self.assertEqual(qs.count(), 2)
    
        def test_unit_measure_validation(self):
            units = 'pounds'
            ingredient = RecipeIngredients(
                name='Beans',
                quantity = 4,
                recipe = self.recipe_a,
                unit = units
            )
            ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        units = ['naira', 'dollars']
        with self.assertRaises(ValidationError):
            for unit in units:
                ingredient = RecipeIngredients(
                    name='Beans',
                    quantity = 4,
                    recipe = self.recipe_a,
                    unit = unit
                )
                ingredient.full_clean()
    
    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)