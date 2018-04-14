from django import forms

class UserForm(forms.Model.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model =User
        fields = ['Username','email','password']
