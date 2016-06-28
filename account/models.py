from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=120)
    premon = models.CharField(max_length=120)
    dateNaiss = models.DateField()
    lieuNaiss = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    motdepass = models.CharField(max_length=120)
    
    def __unicode__(self):
        return self.nom
    
    def __str__(self):
        return self.nom
    
    