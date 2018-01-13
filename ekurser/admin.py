from django.contrib import admin
from .model.enums import DzienTygodnia, StatusWniosku, RodzajGrupy
from .model.models import (Student, NauczycielAkademicki,
                           GrupaZajeciowa, Kurs, Opinia, Termin,
                           WniosekOUruchomienieGrupyZajeciowej)
from .model.through_models import (Prowadzenie, KursKurs,
                                   Uczestnictwo, Opieka, Kwalifikacje)


# enums
class DzienTygodniaAdmin(admin.ModelAdmin):
    pass


class StatusWnioskuAdmin(admin.ModelAdmin):
    pass


class RodzajGrupyAdmin(admin.ModelAdmin):
    pass


# models
class StudentAdmin(admin.ModelAdmin):
    pass


class NauczycielAkademickiAdmin(admin.ModelAdmin):
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


# through
class ProwadzenieAdmin(admin.ModelAdmin):
    pass


class KursKursAdmin(admin.ModelAdmin):
    pass


class OpiekaAdmin(admin.ModelAdmin):
    pass


class KwalifikacjeAdmin(admin.ModelAdmin):
    pass


class UczestnictwoAdmin(admin.ModelAdmin):
    pass


admin.site.register(DzienTygodnia, DzienTygodniaAdmin)
admin.site.register(StatusWniosku, StatusWnioskuAdmin)
admin.site.register(RodzajGrupy, RodzajGrupyAdmin)

admin.site.register(Student, StudentAdmin)
admin.site.register(NauczycielAkademicki, NauczycielAkademickiAdmin)
admin.site.register(GrupaZajeciowa, GrupaZajeciowaAdmin)
admin.site.register(Kurs, KursAdmin)
admin.site.register(Opinia, OpiniaAdmin)
admin.site.register(Termin, TerminAdmin)
admin.site.register(WniosekOUruchomienieGrupyZajeciowej, WniosekOUruchomienieGrupyZajeciowejAdmin)

admin.site.register(Prowadzenie, ProwadzenieAdmin)
admin.site.register(KursKurs, KursAdmin)
admin.site.register(Uczestnictwo, UczestnictwoAdmin)
admin.site.register(Opieka, OpiniaAdmin)
admin.site.register(Kwalifikacje, KwalifikacjeAdmin)
