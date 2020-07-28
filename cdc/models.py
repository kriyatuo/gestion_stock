from django.db import models


class Fournisseur(models.Model):
    code = models.CharField(max_length=25)
    nom = models.TextField()

    def __str__(self):
        return self.nom


class Type_personne(models.Model):
    libelle = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return self.libelle


class Livraison(models.Model):
    fournisseur = models.ForeignKey(
        'fournisseur',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()


class Personnes(models.Model):
    Type_personne = models.ForeignKey(
        'Type_personne',
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=25)
    nom = models.TextField()
    prenom = models.TextField()

    def __str__(self):
        return f'Nom : {self.nom}; Prenoms: {self.prenom}'
