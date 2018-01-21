from django.urls import path, include
from ekurser.kontroler.student import StudentHomeView, GroupPickerView
from ekurser.kontroler.views import main_view, clear_db

urlpatterns = [
    path('student/', StudentHomeView.as_view(), name='student_home'),
    path('student/grupy', GroupPickerView.as_view(), name='group_picker'),
    path('', main_view, name='main'),
    path('clear', clear_db, name='clear' )
]
