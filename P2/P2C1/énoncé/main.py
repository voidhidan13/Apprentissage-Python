
#L'utilisateur rentre les valeurs 
nombre_1 = input("Choissisez votre premier nombre")
nombre_2 = input("Choissisez votre second nombre")

#On vérifie si c'est bien des nombres sous forme de string
if nombre_1.isnumeric() and nombre_2.isnumeric():
   #Si c'est le cas on utilise int pour convertir en data numérique
   #Et stocker la valeur de la nouvelle variable
    nombre_1 = int(nombre_1)
    nombre_2 = int(nombre_2)
else :
    #Si c'est des lettres on ferme le programme
    raise SystemExit("Fin du programme")

#L'utilisateur rentre son opérateur
opérateur = input("Choissisez votre opérateur")

#On vérifie si l'opérateur est bien valide
if  opérateur not in ["+", "-", "*", "/"]:
    raise SystemExit("Fin du progamme")

#On procede aux calculs selon l'operateur
if opérateur == "+" :
    résultat = nombre_1 + nombre_2

elif opérateur == "-" :
    résultat = nombre_1 - nombre_2

elif opérateur == "*" :
    résultat = nombre_1 * nombre_2

elif opérateur == "/" :
    if nombre_2 == 0 :
        raise SystemExit ("Fin du programme")

    
    résultat = nombre_1 / nombre_2 
    résultat = round(résultat)

#On affiche la variable selon sa valeur
print(f"Votre Résultat est {résultat}")