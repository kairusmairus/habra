from django import forms

from .models import Article

class PostArtForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('author', 'title', 'text', )

    widgets = {
        'author' : forms.Select(attrs={'class' : 'form-control'}),
        'title' : forms.TextInput(attrs={'class' : 'form-control'}),
        'text' : forms.Textarea(attrs={'class' : 'form-control'}),
    }    