from django import forms
from .models import UserInputSignal

class UserInputSignalForm(forms.ModelForm):

    class Meta:
        model = UserInputSignal
        exclude = ["author"]
