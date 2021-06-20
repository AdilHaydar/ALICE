from django import forms
from .models import Main, MainImage, Contact



class MainForm(forms.ModelForm):

    class Meta:
        model = Main
        fields = ['content']

class MainImageForm(forms.ModelForm):

    image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'multiple':True,}))

    class Meta:
        model = MainImage
        fields = ['image']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ['status','timestamp']