from django import forms
from src.hitmens.models import User, Hitmen



class AssignSubordinatesForm(forms.Form):

    subordinates = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email', None)
        super().__init__(*args, **kwargs)
        self.fields['subordinates'].queryset = Hitmen.objects.get_subordinates_all(email).exclude(user__is_active=False)

