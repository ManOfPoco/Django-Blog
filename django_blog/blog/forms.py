from django import forms
from .models import Post, Category


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(strip=False, widget=forms.TextInput(attrs={
        'type': "text",
        'class': 'form-control rounded border border-secondary',
        'id': 'floatingInput',
        'placeholder': 'Post Title...'
    }))

    body = forms.CharField(strip=False, widget=forms.Textarea(attrs={
        'type': "text",
        'class': 'form-control rounded border border-secondary',
        'id': 'floatingInput',
        'placeholder': 'Write your post...'
    }))

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'category']
