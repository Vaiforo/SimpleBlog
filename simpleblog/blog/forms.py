from django import forms

from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'titleInput', 'class': 'form-control', 'type': 'text'}),
            'content': forms.Textarea(
                attrs={'id': 'contentTextarea', 'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'titleInput', 'class': 'form-control', 'type': 'text'}),
            'content': forms.Textarea(
                attrs={'id': 'contentTextarea', 'class': 'form-control'}),
        }
