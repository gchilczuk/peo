from django.urls import path, include
from ekurser.kontroler.student import StudentHomeView, GroupPickerView
from ekurser.kontroler.pracownik import TeacherHomeView, PetitionListView, PetitionView
from ekurser.kontroler.views import main_view, clear_db

urlpatterns = [
    path('', main_view, name='main'),
    path('student/', StudentHomeView.as_view(), name='student_home'),
    path('student/grupy/', GroupPickerView.as_view(), name='group_picker'),
    path('pracownik/', TeacherHomeView.as_view(), name='teacher_home'),
    path('pracownik/wnioski', PetitionListView.as_view(), name='petition_list'),
    path('pracownik/wnioski/<nr>', PetitionView.as_view(), name='petition'),
    path('clear/', clear_db, name='clear' )
]

