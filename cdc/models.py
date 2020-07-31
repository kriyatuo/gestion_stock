from django.db import models
from django.db.models.signals import *


class Fournisseur(models.Model):
    code = models.CharField(
        verbose_name='le code du fournisseur', max_length=25)
    nom_fournisseur = models.CharField(
        "le nom de l'organisme fournisseur", max_length=100)

    def __str__(self):
        return self.nom_fournisseur

    class Meta:
        verbose_name = 'Fournisseur'
        verbose_name_plural = 'Fournisseurs'


class Type_personne(models.Model):
    libelle = models.CharField(
        verbose_name='la personne qui récupère les médicaments', max_length=70)
    description = models.TextField(
        verbose_name='description du type de personne')

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name = 'Type de personne'
        verbose_name_plural = 'Type de personnes'


class Livraison(models.Model):
    fournisseur = models.ForeignKey(
        'fournisseur',
        on_delete=models.CASCADE,
        verbose_name='le fournisseur de la livraison'
    )
    date = models.DateField(verbose_name='date de livraison')

    def __str__(self):
        return '{}, {}'.format(self.fournisseur, self.date)

    class Meta:
        verbose_name = 'Livraision'
        verbose_name_plural = 'Livraisons'


class Personne(models.Model):
    Type_personne = models.ForeignKey(
        'Type_personne',
        on_delete=models.CASCADE,
        verbose_name='la personne qui récupère les médicaments'
    )
    code = models.CharField(verbose_name='code personne', max_length=25)
    nom = models.CharField(verbose_name='nom de la personne', max_length=40)
    prenom = models.CharField(
        verbose_name='prenom de la personne', max_length=50)

    def __str__(self):
        return '{} {}'.format(self.nom, self.prenom)

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'Personnes'


class Medicament(models.Model):
    nom_medicament = models.CharField(
        verbose_name='nom du Médicament', max_length=30)
    alerte = models.CharField(
        verbose_name='seuil à ne pas franchir', max_length=70)

    def __str__(self):
        return self.nom_medicament

    class Meta:
        verbose_name = 'Médicament'
        verbose_name_plural = 'Médicaments'


class Recuperation(models.Model):
    personne = models.ForeignKey(
        'Personne',
        on_delete=models.CASCADE,
    )
    medicaments = models.ForeignKey(
        'Medicament',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    quantite = models.FloatField(
        verbose_name='Quantité recuperée', max_length=10)

    def __str__(self):
        return '{}, {}, {}'.format(self.personnes, self.medicaments, self.quantite)

    class Meta:
        verbose_name = 'Recuperation'
        verbose_name_plural = 'Recuperations'


class Batch(models.Model):
    Livraison = models.ForeignKey(
        'Livraison',
        on_delete=models.CASCADE,
    )
    medicament = models.ForeignKey(
        'Medicament',
        on_delete=models.CASCADE,
    )
    bacth_id = models.CharField(max_length=25)
    quantite_batch = models.FloatField(max_length=10)

    def __str__(self):
        return '{}, {}'.format(self.bacth_id, self.Medicaments)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batch'
