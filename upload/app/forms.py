from django import forms
from .models import UploadHander as up

class UploadForm(forms.ModelForm):
    class Meta:
        model = up
        fields = ('file', )