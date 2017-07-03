# -*- coding: utf-8 -*-

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Restaurant(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom
@python_2_unicode_compatible
class Menu(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    restaurant = models.ForeignKey('Restaurant')


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.titre

@python_2_unicode_compatible
class Plat(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    menu = models.ForeignKey('Menu')
    def __str__(self):
        return self.titre
