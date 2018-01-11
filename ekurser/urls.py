from django.urls import path, include
from ekurser.kontroler.views import hello_world

urlpatterns = [
    path('student/', hello_world, name='student_home'),
]
