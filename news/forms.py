from django import forms
from .models import Category

class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=10)
    your_name = forms.ModelChoiceField(queryset = Category.objects.all())