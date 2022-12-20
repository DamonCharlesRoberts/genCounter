from django import forms

from core.models import Document


#class DocumentForm(forms.ModelForm):
#    class Meta:
#        model = Document
#        fields = ('description','file',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["file"]