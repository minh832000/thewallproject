from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            self.author = kwargs.pop('author', None)
            super().__init__(*args, **kwargs)
    def save(self, commit=True):
        post = super().save(commit=False)

        post.author = self.author
        post.save()
    class Meta:
            model = Post
            fields = ['name_post','experience_required','salary','location','content_post','type_job']

