from django import forms
from src.hits.models import Hit


class FormStatusHit(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('status', )
