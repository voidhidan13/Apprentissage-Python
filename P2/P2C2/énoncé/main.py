#L'utilisateur ecrits ses valeurs

Nombres = input("Choisissez une serie de nombres séparés par des virgules")

#On divise ses valeurs a chaque , 
liste_nombres = Nombres.split(",")
#On vérifie la liste
print(liste_nombres)
#On crée une liste vide pour stocker les entiers a chaque boucle
liste_nombres_entiers = []
#La boucle parcourt la liste 
for nombres_entier in liste_nombres :
     # On vérifie que chaque élement de la liste est bien un numéro
    if not nombres_entier.isnumeric() :
        raise SystemExit("Vous avez rentrer des lettres")
    
     # Si c'est bon on convertie le nombre en data numérique
    nombres_entier = int(nombres_entier)
    #A chaque tour la boucle ajoute la valeur dans la nouvelle liste
    liste_nombres_entiers.append(nombres_entier)

print(liste_nombres_entiers)

#Création d'une variable somme
somme = sum(liste_nombres_entiers)
print("liste_nombres_entiers")