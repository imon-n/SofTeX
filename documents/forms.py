from django import forms
from .models import Document
from .models import My_Document,DocumentFile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'files']


class My_DocumentForm(forms.ModelForm):
    class Meta:
        model = My_Document
        fields = ['title', 'date', 'about']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'date':  forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'about': forms.Textarea(attrs={'class': 'form-control'}),
#         }

class DocumentFileForm(forms.ModelForm):
    class Meta:
        model = DocumentFile
        fields = ['file']
#         widgets = {
#            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#         }