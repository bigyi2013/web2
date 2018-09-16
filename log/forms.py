from django import forms
from .models import Liuyan
class LiuyanForm(forms.ModelForm):
    class Meta:
        model = Liuyan
        fields = ['name', 'text']