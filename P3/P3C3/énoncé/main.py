import csv

#Création de la fonction qui extrait les données 
def extract(file="input.csv") :
    #On crée une liste pour stocker les valeurs dictionnaire
    employés = []
    
    #On ouvre le fichier et le stocke sous la variable data
    with open("input.csv","r") as data :
     
# ANALYSE DU MÉCANISME :
# 1. 'data' est le fichier brut (le texte).
# 2. 'lignes' (DictReader) est le MÉCANISME : il lit les titres (1ère ligne) 
#    pour savoir comment créer les futurs dictionnaires.
# 3. La boucle 'for employé in lignes' est le MOMENT OÙ LE TEXTE DEVIENT DICTIONNAIRE.
#    À chaque tour, 'employé' est un nouveau dictionnaire tout prêt.

        lignes = csv.DictReader(data,delimiter=",")    
        #On boucle chaque employé dans toutes les lignes et on rajoute le dictionnaire dans la liste
        for employé in lignes : 
            employés.append(employé)
    return employés

resultat = extract()
print(resultat)

           

        
    
        
            





# Ne touchez pas le code ci-dessous


#if __name__ == "__main__":
   # main()
