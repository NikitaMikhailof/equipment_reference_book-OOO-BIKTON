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
            'body': 'добавить комментарий'} 
        widgets = {
            'name': forms.HiddenInput(),
        }
    
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = f'{request.user.first_name} {request.user.last_name}'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-label'})

       
 
