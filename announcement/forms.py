from .models import Announcement
from django import forms

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title','announcement',]

    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'time'}))

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}