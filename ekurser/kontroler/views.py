from django.shortcuts import render, redirect
from ekurser.model.through_models import Uczestnictwo


def clear_db(request):
    Uczestnictwo.objects.all().delete()
    return redirect('main')


def main_view(request):
    return  render(request, 'main.html', {})
