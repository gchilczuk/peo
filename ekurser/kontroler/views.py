from django.shortcuts import render, redirect
from ekurser.model.through_models import Uczestnictwo
from ekurser.model.models import GrupaZajeciowa


def clear_db(request):
    Uczestnictwo.objects.all().delete()
    grupy = GrupaZajeciowa.objects.all()
    for grupa in grupy:
        grupa.liczbauczestnikow = 0
        grupa.save()
    grupy[0].liczbauczestnikow = 14
    grupy[0].save()

    return redirect('main')


def main_view(request):
    return  render(request, 'main.html', {})
