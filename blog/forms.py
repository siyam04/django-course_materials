from django import forms
from django.forms import TextInput, Textarea, Select

# App importing
from blog.models import Post


class PostCreateForm(forms.ModelForm):
    """Creating a post"""
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title', 'details', 'author', 'is_active')
        # exclude = ('title',)

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'details': Textarea(attrs={'class': 'form-control'}),
            'author': Select(attrs={'class': 'form-control'}),
            # 'is_active': Select(attrs={'class': 'form-control'}),
        }
