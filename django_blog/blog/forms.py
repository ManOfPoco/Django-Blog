from django import forms
from .models import Post, Category, PostComment


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


class PostCommentForm(forms.ModelForm):

    comment = forms.CharField(strip=False, widget=forms.Textarea(attrs={
        'type': "text",
        'class': 'form-control rounded border border-secondary',
        'id': 'floatingInput',
        'placeholder': 'Write your comment...',
        'style': 'resize:none'
    }))

    class Meta:
        model = PostComment
        fields = ['comment']
