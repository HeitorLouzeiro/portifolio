from dataclasses import fields
from django import forms

from .models import About, BarProgress, Card, MiniCard, PersonalData


class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = [
            'name',
            'profession',
            'title',
            'whatsapp',
        ]


class MiniCardForm(forms.ModelForm):
    class Meta:
        model = MiniCard
        exclude = ['skills']


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
