from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content'] 

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Blog.objects.filter(title__icontains = title)
        if qs.exists():
            self.add_error('title', f'{title} is already in use. Please input another title.')

class OldBlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    """
    def clean_title(self):
        cleaned_data = self.cleaned_data
        print("Cleaned data: ", cleaned_data)
        title = cleaned_data.get("title")
        if title.lower().strip() == "my company":
           raise forms.ValidationError ('The title is taken')
        print("Title: ", title)
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print("All data : ", cleaned_data)
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "my company":
            self.add_error('title', 'This title is taken')
        
        if "weapon" in title.lower() or "weapon" in content.lower():
            self.add_error('content', 'the word is already in the title field')
            raise forms.ValidationError("weapon is not allowed")
        print("Title: ", title)
        return cleaned_data
    """    