"""Kontroler dla widoków pracownika"""

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from ekurser.DTO.navigation import Location, Navigation, Postback
from ekurser.DTO.pracownik import Wniosek
from ekurser.model.models import NauczycielAkademicki, WniosekOUruchomienieGrupyZajeciowej
from .forms import petitionJudgeForm


class TeacherHomeView(View):
    """Widok domowy pracownika"""

    user = NauczycielAkademicki.objects.get(id=1)

    def get(self, request):
        location = [Location('Home', reverse('teacher_home'))]
        context = {'navigation': Navigation(str(self.user), location, uid=self.user.id)}

        return render(request, 'wnioski/tHome.html', context)


class PetitionListView(View):
    """Widok listy wniosków do rozpatrzenia"""

    user = NauczycielAkademicki.objects.get(id=1)


    def get(self, request):
        location = [Location('Home', reverse('teacher_home')),
                    Location('wnioski o uruchomienie grupy', reverse('petition_list'))]
        wnioski = []
        for wniosek in WniosekOUruchomienieGrupyZajeciowej.objects.filter(zgodapelnomocnika=None):
            wnioski.append(
                Wniosek(
                    numer=f'{wniosek.nrwniosku//10000}-{wniosek.nrwniosku%10000}',
                    status=wniosek.statuswniosku.nazwa,
                    kurs=wniosek.grupazajeciowa.kurs.nazwakursu,
                    skladajacy=str(wniosek.student),
                    prowadzacy=', '.join([str(prow) for prow in wniosek.grupazajeciowa.prowadzacy.all()]) or "<brak>",
                    zapisanych=wniosek.grupazajeciowa.liczbauczestnikow,
                    rodzaj=wniosek.grupazajeciowa.rodzajgrupy.nazwa,
                    sala=wniosek.grupazajeciowa.termin.sala,
                    termin=f'{wniosek.grupazajeciowa.termin.dzien.nazwa } {wniosek.grupazajeciowa.termin.godzina } ' if wniosek.grupazajeciowa.termin.dzien else '<brak>',
                    opinia='<brak>',
                    id=wniosek.id
                )
            )
        context = {'navigation': Navigation(str(self.user), location, uid=self.user.id),
                   'wnioski': wnioski}
        return render(request, 'wnioski/wnioskiBrowser.html', context)


class PetitionView(View):
    """Widok rozpatrywania wniosku"""

    user = NauczycielAkademicki.objects.get(id=1)

    wniosek = None

    def get(self, request, nr):
        location = [Location('Home', reverse('teacher_home')),
                    Location('wnioski o uruchomienie grupy', reverse('petition_list')),
                    Location(nr, reverse('petition', args=[nr]))]
        self.wniosek = WniosekOUruchomienieGrupyZajeciowej.objects.get(id=nr)

        context = {'navigation': Navigation(str(self.user), location, uid=self.user.id),
                   'wniosek': self.create_wniosek_dto()}
        return render(request, 'wnioski/wniosek.html', context)

    def post(self, request, nr):
        postback = Postback()
        location = [Location('Home', reverse('teacher_home')),
                    Location('wnioski o uruchomienie grupy', reverse('petition_list')),
                    Location(nr, reverse('petition', args=[nr]))]
        self.wniosek = WniosekOUruchomienieGrupyZajeciowej.objects.get(id=nr)
        form = petitionJudgeForm(request.POST)

        if form.is_valid():
            self.wniosek.rozpatrz(bool(int(form.cleaned_data['zgoda'])))

            if self.wniosek.zgodapelnomocnika:
                postback.message = 'Wniosek został zatwierdzony'
            else:
                postback.message = 'Wniosek został odrzucony'
                postback.success = False
        else:
            postback.success = False
            postback.message = "Coś poszło nie tak"

        context = {'navigation': Navigation(str(self.user), location, uid=self.user.id),
                   'wniosek': self.create_wniosek_dto(), 'postback': postback}
        return render(request, 'wnioski/wniosek.html', context)

    def create_wniosek_dto(self):
        """Twordzy obiekt DTO na podstawie wniosku"""
        if self.wniosek.zgodapelnomocnika is None:
            zgoda = 'Brak decyzji'
        elif self.wniosek.zgodapelnomocnika:
            zgoda = 'Tak'
        else:
            zgoda = 'Nie'

        if self.wniosek.grupazajeciowa.termin.dzien:
            termin = f'{self.wniosek.grupazajeciowa.termin.dzien.nazwa } {self.wniosek.grupazajeciowa.termin.godzina } '
        else:
            termin = '<brak>',

        return Wniosek(numer=f'{self.wniosek.nrwniosku//10000}-{self.wniosek.nrwniosku%10000}',
                       status=self.wniosek.statuswniosku.nazwa,
                       kurs=self.wniosek.grupazajeciowa.kurs.nazwakursu,
                       skladajacy=str(self.wniosek.student),
                       prowadzacy=', '.join(
                           [str(prow) for prow in self.wniosek.grupazajeciowa.prowadzacy.all()]) or "<brak>",
                       zapisanych=self.wniosek.grupazajeciowa.liczbauczestnikow,
                       rodzaj=self.wniosek.grupazajeciowa.rodzajgrupy.nazwa,
                       sala=self.wniosek.grupazajeciowa.termin.sala,
                       termin=termin,
                       opinia='<brak>',
                       zgoda=zgoda,
                       id=self.wniosek.id)
