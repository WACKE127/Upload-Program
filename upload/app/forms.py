from django import forms
from .models import UploadHandler as up

class UploadForm(forms.ModelForm):
    class Meta:
        model = up
        fields = ('file', )