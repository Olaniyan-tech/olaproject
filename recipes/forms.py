from django import forms

from .models import Recipe, RecipeIngredients, RecipeIngredientsImage


class RecipeIngredientImageForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredientsImage
        fields = ['recipe', 'image']


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(help_text='You ask for help!!! <a href="/contact">Contact Us</a>')
    #descriptions = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control", "rows" : 3, "style": "min-height: 100px;"}))
    class Meta:
        model = Recipe
        fields = ['name', 'descriptions', 'directions']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'placeholder' : f'Recipe {str(field)}',
                'class' : 'form-control',}
                #'hx-post' : '.'}
                # 'hx-trigger' : 'keyup changed delay:400ms',
                # 'hx-target' : '#recipe-container',
                # 'hx-swap' : 'outerHTML'}
            
            self.fields[str(field)].widget.attrs.update(new_data)
        # self.fields['name'].label = ''
        #self.fields['name'].widget.attrs.update({'class' : 'form-control-2'})
        self.fields['descriptions'].widget.attrs.update({'rows' : '2'})
        self.fields['directions'].widget.attrs.update({'rows' : '5'})

class RecipeIngredientsForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['name', 'quantity', 'unit']