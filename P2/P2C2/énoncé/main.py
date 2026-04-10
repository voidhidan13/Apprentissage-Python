#L'utilisateur ecrits ses valeurs

Nombres = input("Choisisez une serie de nombres séparés par des virgules")

#On divise ses valeurs a chaque , 
liste_nombres = Nombres.split(",")
#On vérifie la liste
print(liste_nombres)
#On crée une liste vide pour stocker les entiers a chaque boucle
liste_nombres_entiers = []
#La boucle parcourt la liste est transforme la valeur en entier a chaque tour
for nombres_entier in liste_nombres :
    nombres_entier = int(nombres_entier)
    #A chaque tour la boucle ajoute la valeur dans la nouvelle liste
    liste_nombres_entiers.append(nombres_entier)

print(liste_nombres_entiers)