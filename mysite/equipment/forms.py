from django import forms
from .models import Comment


class SearchForm(forms.Form):
    query = forms.CharField(label='Запрос')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']    
        labels = {
            'name': 'имя',
            'body': 'комментарий'}

       
 
