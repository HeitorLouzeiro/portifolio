from django import forms

from .models import About, BarProgress, Card, PersonalData, SocialMedia


class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = [
            'name',
            'profession',
            'title',
            'whatsapp',
        ]
