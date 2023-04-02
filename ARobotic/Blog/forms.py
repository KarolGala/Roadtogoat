from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    website = forms.URLField(required=False)
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body','website')