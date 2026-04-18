import csv
#FONCTION D'EXTRACTION
# --- On ouvre avec l'argument lecture, on stocke les elements dans data
# --- Reader est un lecteur qui prend les deux premieres ligne comme en-tete
# --  la boucle for aide le lecteur à crée un dictionnaire et ajouter les etiquettes dans un dictionnaire
#                        NOM + HEURES TRAVAILLES
# --- On ajoute chaque dictionnaire dans la liste
def extraction(file="input.csv") :
    #On crée la liste qui va accueullir les valeurs
    données_brutes = []
    
    with open(file, "r") as data :
        reader = csv.DictReader(data,delimiter=',')
        for employé in reader : 
           données_brutes.append(employé)
    return données_brutes
#FONCTION TRANSFORMATION
# --- On crée la nouvelle liste pour accueuillir les résultats calcul
# --- La boucle for calcule chaque salaire dans la liste d'extraction
#  -- On crée le nouveau dictionnaire pour chaque clé et la nouvelle valeur clé
# --- On ajoute chaque dictionnaire dans la liste
def transform(données_brutes) :
    #On crée la liste qui va accueullir les valeurs
    données_calculés = []
    
    for salaire in données_brutes :
        nom_employe = salaire["nom"]
        calcul_salaire = int(salaire["heures_travaillees"]) * 15
        nouveau_dictionnaire = {
            "nom": nom_employe,
            "salaire": calcul_salaire
        }   
        
        données_calculés.append(nouveau_dictionnaire)
    return données_calculés

def load(données_calculés, file="output.csv") :
    with open(file, "w", newline="", encoding="utf-8") as data_csv:
        en_tete = ["nom","salaire"]
        writer = csv.DictWriter(data_csv,fieldnames=en_tete)
        writer.writeheader()
        writer.writerows(données_calculés)


def main():
    # 1. On extrait et on stocke le résultat
    mes_donnees_brutes = extraction()
    
    # 2. On passe les brutes à la machine transform, et on stocke le résultat
    données_calculés = transform(mes_donnees_brutes)
    
    # 3. On donne l'ordre d'écrire le résultat (pas besoin du '=' !)
    # (Pas besoin non plus de préciser file="output.csv" car c'est déjà ton paramètre par défaut)
    load(données_calculés)
    
    # 4. On célèbre !
    print("Export réussi !")


if __name__ == "__main__":
    main()
