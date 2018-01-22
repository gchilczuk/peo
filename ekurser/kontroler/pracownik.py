from django.shortcuts import render
from django.urls import reverse
from django.views import View

from ekurser.DTO.navigation import Location, Navigation, Postback
from ekurser.DTO.pracownik import Wniosek
from ekurser.model.models import NauczycielAkademicki, WniosekOUruchomienieGrupyZajeciowej
from .forms import petitionJudgeForm


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
        context = {'navigation': Navigation(str(user), location, uid=user.id),
                   'wnioski': wnioski}
        return render(request, 'wnioski/wnioskiBrowser.html', context)


class PetitionView(View):
    def get(self, request, nr):
        user = NauczycielAkademicki.objects.get(id=1)
        location = [Location('Home', reverse('teacher_home')),
                    Location('wnioski o uruchomienie grupy', reverse('petition_list')),
                    Location(nr, reverse('petition', args=[nr]))]

        wniosek = WniosekOUruchomienieGrupyZajeciowej.objects.get(id=nr)
        zgoda = 'Brak decyzji'
        if wniosek.zgodapelnomocnika:
            zgoda = 'Tak'
        elif wniosek.zgodapelnomocnika is not None:
            zgoda = 'Nie'
        wniosek = Wniosek(numer=f'{wniosek.nrwniosku//10000}-{wniosek.nrwniosku%10000}',
                          status=wniosek.statuswniosku.nazwa,
                          kurs=wniosek.grupazajeciowa.kurs.nazwakursu,
                          skladajacy=str(wniosek.student),
                          prowadzacy=', '.join(
                              [str(prow) for prow in wniosek.grupazajeciowa.prowadzacy.all()]) or "<brak>",
                          zapisanych=wniosek.grupazajeciowa.liczbauczestnikow,
                          rodzaj=wniosek.grupazajeciowa.rodzajgrupy.nazwa,
                          sala=wniosek.grupazajeciowa.termin.sala,
                          termin=f'{wniosek.grupazajeciowa.termin.dzien.nazwa } {wniosek.grupazajeciowa.termin.godzina } ' if wniosek.grupazajeciowa.termin.dzien else '<brak>',
                          opinia='<brak>',
                          zgoda=zgoda,
                          id=wniosek.id)
        context = {'navigation': Navigation(str(user), location, uid=user.id),
                   'wniosek': wniosek}
        return render(request, 'wnioski/wniosek.html', context)

    def post(self, request, nr):
        postback = Postback()
        user = NauczycielAkademicki.objects.get(id=1)
        location = [Location('Home', reverse('teacher_home')),
                    Location('wnioski o uruchomienie grupy', reverse('petition_list')),
                    Location(nr, reverse('petition', args=[nr]))]

        wniosek = WniosekOUruchomienieGrupyZajeciowej.objects.get(id=nr)
        form = petitionJudgeForm(request.POST)
        if form.is_valid():
            kurs_id = form.cleaned_data['kurs']
            wniosek.zgodapelnomocnika = bool(int(form.cleaned_data['zgoda']))
            wniosek.save()
            postback.message = 'Wniosek został '
            if wniosek.zgodapelnomocnika:
                postback.message += 'zatwierdzony'
            else:
                postback.message += 'odrzucony'
                postback.success = False
        else:
            postback.success = False
            postback.message = "Coś poszło nie tak"

        zgoda = 'Brak decyzji'
        if wniosek.zgodapelnomocnika:
            zgoda = 'Tak'
        elif wniosek.zgodapelnomocnika is not None:
            zgoda = 'Nie'

        wniosek_dto = Wniosek(numer=f'{wniosek.nrwniosku//10000}-{wniosek.nrwniosku%10000}',
                              status=wniosek.statuswniosku.nazwa,
                              kurs=wniosek.grupazajeciowa.kurs.nazwakursu,
                              skladajacy=str(wniosek.student),
                              prowadzacy=', '.join(
                                  [str(prow) for prow in wniosek.grupazajeciowa.prowadzacy.all()]) or "<brak>",
                              zapisanych=wniosek.grupazajeciowa.liczbauczestnikow,
                              rodzaj=wniosek.grupazajeciowa.rodzajgrupy.nazwa,
                              sala=wniosek.grupazajeciowa.termin.sala,
                              termin=f'{wniosek.grupazajeciowa.termin.dzien.nazwa } {wniosek.grupazajeciowa.termin.godzina } ' if wniosek.grupazajeciowa.termin.dzien else '<brak>',
                              opinia='<brak>',
                              zgoda=zgoda,
                              id=wniosek.id)
        context = {'navigation': Navigation(str(user), location, uid=user.id),
                   'wniosek': wniosek_dto, 'postback': postback}
        return render(request, 'wnioski/wniosek.html', context)
