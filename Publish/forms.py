from django import forms
from .models import *


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ['column','notes']

class PublishArticleForm(forms.ModelForm):

    title =forms.CharField(
        max_length=300,
        label="文章分类:",
        # required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入文章分类！',
        }),
    )
    class Meta:
        model = PublishArticle
        fields = ['title','body']
