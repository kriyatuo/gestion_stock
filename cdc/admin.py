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


class PersonneAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'prenom')


class RecuperationAdmin(admin.ModelAdmin):
    list_display = ('personne', 'date', 'quantite')
    list_filter = ('date',)


class BatchAdmin(admin.ModelAdmin):
    list_display = ('bacth_id', 'medicament', 'quantite_batch')


admin.site.register(Livraison, LivraisonAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Type_personne)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Medicament)
admin.site.register(Recuperation, RecuperationAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.unregister(Group)
