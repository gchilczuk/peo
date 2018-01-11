from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):

    context = {
        'helo': 'No cześć',
        'title': 'Tytuł'
    }

    return render(request, 'base.html', context )

# zrobić DTO - czyli obiekt o konkretnej strukturze, którą będzie wyświetlał template
