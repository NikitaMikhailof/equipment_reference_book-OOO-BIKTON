from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='логин')
    password = forms.CharField(label='пароль')

    class Meta:
        fields = ['username', 'password']   
     
       
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.errors.items():
            v.widget.attrs.update({'class': 'message-error'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control-login form-label-login'})    

    