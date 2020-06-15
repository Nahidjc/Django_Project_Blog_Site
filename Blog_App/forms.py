from django import forms
from Blog_App.models import Comment,Blog
class ComentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields =('comment',)
