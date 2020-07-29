from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'Gestionnaire de Stock'


class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('fournisseur', 'date')
    list_filter = ('date',)


admin.site.register(Livraison, LivraisonAdmin)
admin.site.register(Fournisseur)
admin.site.register(Type_personne)
admin.site.register(Personnes)
admin.site.register(Medicaments)
admin.site.register(Recuperation)
admin.site.register(Batch)
admin.site.unregister(Group)
