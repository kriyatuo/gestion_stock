from django.db import models


class Fournisseur(models.Model):
    code = models.CharField(max_length=25)
    nom_fournisseur = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_fournisseur


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
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format({self.nom}, {self.prenom})


class Medicaments(models.Model):
    nom_medicament = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_medicament


class Recuperation(models.Model):
    Personnes = models.ForeignKey(
        'Personnes',
        on_delete=models.CASCADE,
    )
    Medicaments = models.ForeignKey(
        'Medicaments',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    quantite = models.FloatField(max_length=10)

    def __str__(self):
        return '{} {} {}'.format({self.Personnes}, {self.Medicaments}, {self.quantite})


class Batch(models.Model):
    Livraison = models.ForeignKey(
        'Livraison',
        on_delete=models.CASCADE,
    )
    Medicaments = models.ForeignKey(
        'Medicaments',
        on_delete=models.CASCADE,
    )
    bacth_id = models.FloatField()
    quantite_batch = models.FloatField(max_length=10)

    def __str__(self):
        return '{} {}'.format({self.bacth_id}, {self.Medicaments})
