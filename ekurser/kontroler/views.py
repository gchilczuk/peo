from django.shortcuts import render, redirect
from ekurser.model.through_models import Uczestnictwo
from ekurser.model.models import GrupaZajeciowa, WniosekOUruchomienieGrupyZajeciowej


def clear_db(request):
    Uczestnictwo.objects.all().delete()
    grupy = GrupaZajeciowa.objects.all().order_by('-liczbamiejsc')
    for grupa, u in zip(grupy,[16, 14, 0]):
        grupa.liczbauczestnikow = u
        grupa.save()

    for wniosek in WniosekOUruchomienieGrupyZajeciowej.objects.all():
        wniosek.zgodapelnomocnika = None
        wniosek.save()

    return redirect('main')


def main_view(request):
    return render(request, 'main.html', {})
