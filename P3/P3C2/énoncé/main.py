# import du module Beautifulsoup uniquement
from bs4 import BeautifulSoup

# Lecture et ouverture du index avec creation variable file
with open("index.html", 'r') as file:
    # Création variable soup pour recuperer les elements 
    soup = BeautifulSoup(file, 'html.parser')

#Récupération du titre
titre = soup.title.text


h1 = soup.find(id="titre").text

#On récupere tous les élements li
Liste_Produits = soup.find_all("li")

#Création du dictionnaire vide
tous_les_produits = {}

#Pour chaque produit dans la liste
for produit in Liste_Produits:
    #On récupere le nom
    name = produit.find("h2").text
   
    # --- LE PRIX ---
    # MÉMO :
    # 1. find("p", ...).text -> Récupère la phrase entière dans la balise (ex: "Prix : 10€").
    # 2. split(" ")[-1]      -> Coupe la phrase à chaque espace, et garde uniquement le dernier morceau ("10€").
    # 3. replace(...)        -> Efface le symbole Euro (le normal ET le buggé sous Windows) pour isoler le chiffre ("10").
    # 4. float() * 1.2       -> Transforme le texte "10" en vrai nombre (float) pour pouvoir faire la multiplication !
    
    
    price = produit.find("p", class_="price").text
    #On nettoye le symbole euros et le bug w11
    price = price.split(" ")[-1].replace("€", "").replace("â‚¬", "")
    #On convertie en dollar
    price_dollar = float(price) * 1.2

   
   # --- LA DESCRIPTION ---
    # MÉMO : 
    # 1. find_all("p")[-1] -> On attrape la TOUTE DERNIÈRE boîte <p> du produit.
    # 2. .text             -> On lit la phrase entière à l'intérieur ("Description : Lorem ipsum...").
    # 3. .replace(...)     -> On nettoie le texte en effaçant l'étiquette "Description : " du début !
    descriptions = produit.find_all("p")[-1].text.replace("Description : ", "")
    
    # ICI : On crée le tiroir et on range tout dedans avec = et {}
    tous_les_produits[name] = {
        "prix": f"{price_dollar} $",
        "description": descriptions
    }

print(tous_les_produits)

