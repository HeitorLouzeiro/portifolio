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
            'cover',
        ]


class MiniCardForm(forms.ModelForm):
    class Meta:
        model = MiniCard
        exclude = ['skills']


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


class BarProgressForm(forms.ModelForm):
    class Meta:
        model = BarProgress
        fields = '__all__'


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
