from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, label='Parola', widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label='Parolayı Doğrula', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

    def clean_confirm(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parolalar Eşleşmiyor')

        return confirm

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    
"""
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if (confirm and password) and (password != confirm):
            raise forms.ValidationError('Parolalar Eşleşmiyor')

        values = {
            "username":username,
            "password":password,
            "confirm":confirm,
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
        }

        return values
"""

    
