from django import forms
from .models import *


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ['column','notes']

class PublishArticleForm(forms.ModelForm):
    class Meta:
        model = PublishArticle
        fields = ['title','body']
