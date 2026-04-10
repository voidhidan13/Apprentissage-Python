def calcul_salaire_mensuel (salaire_annuel, mois_travaillés) : 
   salaire_mensuel = salaire_annuel / mois_travaillés
   return salaire_mensuel 

def calcul_salaire_hebdomadaire (salaire_mensuel,semaines_travaillés) :
   salaire_hebdomadaire = salaire_mensuel / semaines_travaillés
   return salaire_hebdomadaire

def calcul_salaire_horaire (salaire_hebdomadaire,heures_travaillés) :
   salaire_horaire = salaire_hebdomadaire / heures_travaillés
   return salaire_horaire

#L'utilisateur definit son salaire annuel et ses heures travaillés
salaire_annuel = input("Saissisez votre Salaire annuel")
heures_travaillés = input("Saissisez vos heures travaillés")

#Si ce n'est pas des nombres on s'arrete
if not salaire_annuel.isnumeric() or not heures_travaillés.isnumeric() :
   raise SystemError("Veuillez rentrez des nombres")

#Sinon on convertit
salaire_annuel = int(salaire_annuel)
heures_travaillés = int(heures_travaillés)

#On donne la valeur 4 a semaine travaillés
semaines_travaillés = 4 
mois_travaillés = 12

#On appelle nos fonctions avec les variables précedentes en parametres

salaire_mensuel = calcul_salaire_mensuel (salaire_annuel,mois_travaillés)
salaire_hebdomadaire = calcul_salaire_hebdomadaire (salaire_mensuel, 4)

#On appelle la derniere fonction tout en arrondissant le résultat
salaire_horaire = round(calcul_salaire_horaire(salaire_hebdomadaire, heures_travaillés), 2)


print(f"Votre Salaire horaire est de : {salaire_horaire} euros")