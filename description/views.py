from unicodedata import category
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.core.cache import cache
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()


def description(request,cat,idannonce):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()

    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      data= geta.description_fonction(database=database,categorie=cat,idannonce=idannonce)
      list= geta.description_and_home_categorie_plus(database,cat)
      nombre_de_vues = geta.nombres_des_vus_fonction(database=database,idannonce=idannonce)
      return render(request,"description/description.html", {"uid":uid,"data":data,"list":list,"vues":nombre_de_vues})
    #on recuperer les donnes de l'annonce 
    data = geta.description_fonction(database=database,categorie=cat,idannonce=idannonce)
    list= geta.description_and_home_categorie_plus(database,cat)
    nombre_de_vues = geta.nombres_des_vus_fonction(database=database,idannonce=idannonce)
    print(data)

    return render(request,"description/description.html", {"uid":uid,"data":data,"list":list,"vues":nombre_de_vues})
