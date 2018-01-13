from django.shortcuts import render
from django.urls import reverse
from django.views import View
from ekurser.DTO.student import Navigation, Location


class StudentHomeView(View):
    def get(self, request):
        location = [Location('Home', reverse('student_home'))]
        context = {'nav': Navigation('Jaś Fasola', location)}

        return render(request, 'grupy/sHome.html', context)


class GroupPickerView(View):
    def get(self, request):
        location = [Location('Home', reverse('student_home')),
                    Location('przeglądanie grup', reverse('group_picker'))]
        context = {'nav': Navigation('Jaś Fasola', location)}

        return render(request, 'grupy/grupyForm.html', context)

    def post(self, request):
        pass
