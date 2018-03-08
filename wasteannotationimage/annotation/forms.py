from django import forms
from .models import Image

class NewImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
