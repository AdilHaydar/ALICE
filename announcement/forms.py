from .models import Announcement
from django import forms

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title','announcement','deadline_at']

    deadline_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}