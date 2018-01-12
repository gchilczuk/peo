from django.contrib import admin
from .model.users import Student, NauczycielAkademicki
from .model.enums import DzienTygodnia, StatusWniosku, RodzajGrupy
from .model.studies import (GrupaZajeciowa, Kurs, Opinia, Termin,
                            WniosekOUruchomienieGrupyZajeciowej)


# users
class StudentAdmin(admin.ModelAdmin):
    pass


class NauczycielAkademickiAdmin(admin.ModelAdmin):
    pass


# enums
class DzienTygodniaAdmin(admin.ModelAdmin):
    pass


class StatusWnioskuAdmin(admin.ModelAdmin):
    pass


class RodzajGrupyAdmin(admin.ModelAdmin):
    pass


class GrupaZajeciowaAdmin(admin.ModelAdmin):
    pass


class KursAdmin(admin.ModelAdmin):
    pass


class OpiniaAdmin(admin.ModelAdmin):
    pass


class TerminAdmin(admin.ModelAdmin):
    pass


class WniosekOUruchomienieGrupyZajeciowejAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(NauczycielAkademicki, NauczycielAkademickiAdmin)

admin.site.register(DzienTygodnia, DzienTygodniaAdmin)
admin.site.register(StatusWniosku, StatusWnioskuAdmin)
admin.site.register(RodzajGrupy, RodzajGrupyAdmin)

admin.site.register(GrupaZajeciowa, GrupaZajeciowaAdmin)
admin.site.register(Kurs, KursAdmin)
admin.site.register(Opinia, OpiniaAdmin)
admin.site.register(Termin, TerminAdmin)
admin.site.register(WniosekOUruchomienieGrupyZajeciowej, WniosekOUruchomienieGrupyZajeciowejAdmin)
