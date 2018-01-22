from django import forms
from ekurser.model.enums import RodzajGrupy

class grupyForm(forms.Form):
    CHOICES = [('', 'wszystkie')] + [(rodz.id, rodz.nazwa ) for rodz in RodzajGrupy.objects.all()]
    nazwa = forms.CharField(label="Nazwa kursu", required=False)
    rodzaj = forms.ChoiceField(label='Rodzaj grupy', required=False, choices=CHOICES)

class grupyConfirmForm(forms.Form):
    nazwa = forms.CharField(required=False)
    rodzaj = forms.CharField(required=False)
    student = forms.CharField()
    grupa = forms.CharField()


class petitionJudgeForm(forms.Form):
    kurs = forms.CharField()
    zgoda = forms.CharField()
