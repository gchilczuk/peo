from django.contrib import admin
from .model.users import Student, Nauczycielakademicki

class StudentAdmin(admin.ModelAdmin):
    pass


class NauczycielAkademickiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Nauczycielakademicki, NauczycielAkademickiAdmin)