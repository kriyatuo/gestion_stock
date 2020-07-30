from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'DASHBOARD PHARMACIE'
admin.site.title = "GESTION STOCK"


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom_fournisseur')


class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('fournisseur', 'date')
    list_filter = ('date',)


class PersonnesAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'prenom')


class RecuperationAdmin(admin.ModelAdmin):
    list_display = ('Personnes', 'date', 'quantite')
    list_filter = ('date',)


class BatchAdmin(admin.ModelAdmin):
    list_display = ('bacth_id', 'Medicaments', 'quantite_batch')


admin.site.register(Livraison, LivraisonAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Type_personne)
admin.site.register(Personnes, PersonnesAdmin)
admin.site.register(Medicaments)
admin.site.register(Recuperation, RecuperationAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.unregister(Group)
