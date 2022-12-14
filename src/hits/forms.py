from django import forms
from src.hits.models import Hit, Hitmen


class FormStatusHitmen(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('status_hitmen', )

class FormAssignedHit(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('assigned', )


class CreateHitFormModel(forms.ModelForm):

    class Meta:
        model = Hit
        fields = ('title', 'target', 'descriptions', 'assigned')

    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email', None)
        super().__init__(*args, **kwargs)
        self.fields['assigned'].queryset = Hitmen.objects.get_subordinates_all(email).exclude(user__is_active=False)
