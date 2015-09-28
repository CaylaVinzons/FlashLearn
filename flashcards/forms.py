from django import forms
from .models import *

class ScanUploadForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = '__all__'

class DocumentEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

class CardEditForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
