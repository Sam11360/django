# -*- coding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from menu.models import Menu, Restaurant

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = u"""<h1>Bienvenue!! dans le restaurant !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'menu/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'menu/addition.html', locals())

def accueil(request):
    """ Afficher tous les menus des restaurants """
    restaurant = Restaurant.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'menu/accueil.html', {'derniers_restaurant': restaurant})



def lire(request, id):
    """ Afficher un article complet """
    pass # Le code de cette fonction est donné un peu plus loin.
