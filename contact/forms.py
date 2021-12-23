from django import forms
from .models import ModelContact


class ModelContactForm(forms.ModelForm):
    class Meta:
        model = ModelContact
        fields = '__all__'
        exclude = ('date_added',)
