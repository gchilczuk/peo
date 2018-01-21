from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from ekurser.DTO.student import Navigation, Location, Group
from ekurser.DTO.postback import Postback
from ekurser.model.enums import RodzajGrupy
from ekurser.model.models import GrupaZajeciowa, Student
from ekurser.model.through_models import Uczestnictwo
from .forms import grupyForm, grupyConfirmForm


class StudentHomeView(View):
    def get(self, request):
        location = [Location('Home', reverse('student_home'))]
        context = {'nav': Navigation('Jaś Fasola', location)}

        return render(request, 'grupy/sHome.html', context)


class GroupPickerView(View):
    def get(self, request):
        location = [Location('Home', reverse('student_home')),
                    Location('przeglądanie grup', reverse('group_picker'))]

        context = {'nav': Navigation('Jaś Fasola', location),
                   'form': grupyForm()}
        return render(request, 'grupy/grupyForm.html', context)

    def post(self, request):
        postback = Postback()
        location = [Location('Home', reverse('student_home')),
                    Location('przeglądanie grup', reverse('group_picker'))]

        form = grupyConfirmForm(request.POST)
        if not form.is_valid():
            postback.ispostback = False
            form = grupyForm(request.POST)
            if not form.is_valid():
                return HttpResponse("Nie działam")

        if postback.ispostback:
            g = GrupaZajeciowa.objects.get(id=form.cleaned_data['grupa'])
            try:
                if not g.dodaj_studenta(Student.objects.get(id=form.cleaned_data['student'])):
                    postback.success = False
                    postback.message = 'Nie możesz zapisać się dwa razy do tej samej grupy!'
            except ValidationError:
                postback.success = False
                postback.message = 'Grupa jest pełna'

        rodzaj, nazwa = form.cleaned_data['rodzaj'], form.cleaned_data['nazwa']
        filters ={'kurs__nazwakursu__contains': nazwa}
        if rodzaj:
            filters['rodzajgrupy_id'] = rodzaj
            rodzaj = (RodzajGrupy.objects.get(id=rodzaj).nazwa, rodzaj)
        grupy = []
        for grupa in GrupaZajeciowa.objects.filter(**filters):
            grupy.append(Group(
                kurs=grupa.kurs.nazwakursu,
                prowadzacy=', '.join([str(prow) for prow in grupa.prowadzacy.all()]) or "<brak>",
                rodzaj=grupa.rodzajgrupy.short(),
                sala=grupa.termin.sala or '<brak>',
                termin=f'{grupa.termin.dzien.nazwa} {grupa.termin.godzina}' if grupa.termin.dzien else '<brak>',
                zapisanych=grupa.studenci.count(),
                miejsc=grupa.liczbamiejsc,
                id=grupa.id
            ))
        context = {'nav': Navigation('Jaś Fasola', location, rodzaj=rodzaj, nazwa=nazwa),
                   'grupy': grupy, 'postback': postback}

        return render(request, 'grupy/grupyBrowser.html', context)

