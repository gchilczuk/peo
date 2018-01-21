from django.shortcuts import render
from django.urls import reverse
from django.views import View

from ekurser.DTO.navigation import Location, Navigation
from ekurser.DTO.pracownik import Wniosek
from ekurser.model.models import NauczycielAkademicki, WniosekOUruchomienieGrupyZajeciowej


class TeacherHomeView(View):
    def get(self, request):
        user = NauczycielAkademicki.objects.get(id=1)
        location = [Location('Home', reverse('teacher_home'))]
        context = {'navigation': Navigation(str(user), location, uid=user.id)}

        return render(request, 'wnioski/tHome.html', context)

class PetitionListView(View):
    def get(self, request):
        user = NauczycielAkademicki.objects.get(id=1)
        location = [Location('Home', reverse('teacher_home')),
                    Location('przeglądanie grup', reverse('petition_list'))]

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
                    termin=f'{wniosek.grupazajeciowa.termin.dzien.nazwa } {wniosek.grupazajeciowa.termin.godzina } 'if wniosek.grupazajeciowa.termin.dzien else '<brak>',
                    opinia='<brak>',
                    id=wniosek.id
                )
            )
        context = {'navigation': Navigation(str(user), location, uid=user.id),
                   'wnioski': wnioski}
        return render(request, 'wnioski/wnioskiBrowser.html', context)


class PetitionView(View):
    def get(self, request, nr):
        user = NauczycielAkademicki.objects.get(id=1)
        location = [Location('Home', reverse('teacher_home')),
                    Location('przeglądanie grup', reverse('petition_list'))]

        wnioski = []
        for wniosek in WniosekOUruchomienieGrupyZajeciowej.objects.filter(zgodapelnomocnika=None, nrwniosku=nr):
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
        context = {'navigation': Navigation(str(user), location, uid=user.id),
                   'wnioski': wnioski}
        return render(request, 'wnioski/wnioskiBrowser.html', context)

    def post(self, request, nr):
        pass