from django.shortcuts import render


def hello_world(request):

    context = {
        'helo': 'No cześć',
        'title': 'Tytuł'
    }

    return render(request, 'base.html', context)
