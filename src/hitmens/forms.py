from django import forms
from src.hitmens.models import User

class ChangeIsActive(forms.ModelForm):

    class Meta:
        model = User
        fields = ('is_active', )
