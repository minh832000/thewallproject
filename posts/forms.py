from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ['name_post','experience_required','salary','location','content_post']
