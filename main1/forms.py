from django import forms
from . import models

class CreateArticle(forms.ModelForm):
  class Meta:
    model = models.Article
    fields = ['title', 'slug', 'body', 'thumb']
    # use the above or '__all__' when you're picking all the fields in your models