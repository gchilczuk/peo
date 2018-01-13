from django.urls import path, include
from ekurser.kontroler.student import StudentHomeView, GroupPickerView

urlpatterns = [
    path('student/', StudentHomeView.as_view(), name='student_home'),
    path('student/grupy', GroupPickerView.as_view(), name='group_picker'),
]
