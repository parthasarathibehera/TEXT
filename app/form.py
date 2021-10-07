from django import forms
from .models import EditorModel


class EditorForm(forms.ModelForm):
    class Meta:
        model = EditorModel
        fields = "__all__"
