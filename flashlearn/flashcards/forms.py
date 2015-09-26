from django import forms
from .models import *

class ScanUploadForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = '__all__'
