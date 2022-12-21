from django import forms

from .models import LogForm


class Loger(forms.ModelForm):
    class Meta:
        model = LogForm
        fields = '__all__'
