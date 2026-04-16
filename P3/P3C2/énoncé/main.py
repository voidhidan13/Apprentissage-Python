# import du module Beautifulsoup uniquement
from bs4 import BeautifulSoup

# Lecture et ouverture du index avec creation variable file
with open("index.html", 'r') as file:
    # Création variable soup pour recuperer les elements 
    soup = BeautifulSoup(file, 'html.parser')

#Récupération du titre
titre = soup.title.text


h1 = soup.find(id="titre").text


#Création du dictionnaire vide
tous_les_produits = {}

#On récupere tous les élements li
Liste_Produits = soup.find_all("li")


#Pour chaque produit dans la liste
for produit in Liste_Produits :
    #on recupere le nom
    name = produit.find("h2").text
   #on recupere le prix
    price = produit.find("p", class_="price").text
    #on coupe la valeur en deux apres l'espace et on prend le dernier element
    price = price.split(" ")[-1].replace("€", "")
    #on ajoute les valeurs au dictionnaire
    tous_les_produits[name] = f"le prix est de : {price}"
    print (tous_les_produits)
    
