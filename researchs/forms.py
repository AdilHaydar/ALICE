from django import forms
from .models import CategoryResearch, Research

class ResearchForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryResearch.objects.all() ,widget=forms.Select(attrs={'class':'ui search dropdown'}))
    class Meta:
        model = Research
        exclude = ('created_at', 'deadline_at')

class CategoryResearchForm(forms.ModelForm):

    class Meta:
        model = CategoryResearch
        fields = '__all__'