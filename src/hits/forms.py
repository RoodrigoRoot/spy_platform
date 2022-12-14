from django import forms
from src.hits.models import Hit


class FormStatusHitmen(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('status_hitmen', )

class FormAssignedHit(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('assigned', )
