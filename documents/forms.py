from django import forms
from .models import Document, My_Document,DocumentFile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'files']


class My_DocumentForm(forms.ModelForm):
    class Meta:
        model = My_Document
        fields = ['title', 'date', 'about']


class DocumentFileForm(forms.ModelForm):
    class Meta:
        model = DocumentFile
        fields = ['file']