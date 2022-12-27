"""
    Title: forms
    Notes:
        - Description: creates a form for people to upload the document to
        - Updated: 2022-12-23
        - Updated by: dcr
"""

from django import forms # for form creation
from core.models import Document # load the Document model created in models

class DocumentForm(forms.ModelForm):
    """
        Name: DocumentForm
        Description: Using core.models.Document, it uploads the document and stores it
        Dependencies:
            - django.forms
            - core.models.Document

    """
    class Meta:
        model = Document
        fields = ["file"]