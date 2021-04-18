from django.forms.widgets import CheckboxSelectMultiple
from .models import MeetingReport, Meeting
from django import forms


class MeetingReportForm(forms.ModelForm):
    """
    category = forms.ModelMultipleChoiceField(
        queryset=MeetingReportCategory.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    """
    class Meta:
        model = MeetingReport
        exclude = ['user', 'created_at']

    def __init__(self, *args, **kwargs):
        super(MeetingReportForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'file':
                continue
            self.fields[field].widget.attrs = {'class':'form-control'}


class MeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        exclude = ['user', 'created_at']
        