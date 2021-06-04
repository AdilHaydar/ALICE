from .models import Shift
from django import forms


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'
