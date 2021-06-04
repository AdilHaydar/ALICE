from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','file']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'file':
                continue
            self.fields[field].widget.attrs = {'class':'form-control'}
