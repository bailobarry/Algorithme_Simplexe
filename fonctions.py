import random  # Importation du module random pour la génération de nombres aléatoires

 # Fonction pour trouver la colonne du pivot dans le tableau
def trouver_pivot(tableau):
    derniere_ligne = tableau[-1]  # La dernière ligne du tableau contient les coûts réduits
    colonne_pivot = None 
    for i in range(len(derniere_ligne) - 1):  # Parcourt les colonnes du tableau
        if derniere_ligne[i] < 0: 
            colonne_pivot = i  
            break  
    return colonne_pivot  # Renvoie la colonne du pivot

 # Fonction pour mettre à jour le tableau en fonction du pivot sélectionné
def mettre_a_jour_tableau(tableau, ligne_pivot, colonne_pivot, valeur_pivot):
    for i in range(len(tableau)): 
        if i != ligne_pivot:  
            multiplicateur = tableau[i][colonne_pivot]  # Obtient le multiplicateur pour annuler le terme pivot
            for j in range(len(tableau[i])):
                tableau[i][j] -= multiplicateur * tableau[ligne_pivot][j] 
            tableau[i][colonne_pivot] = 0  # Met à zéro le terme correspondant à la colonne du pivot
    # Normalisation de la ligne du pivot
    for j in range(len(tableau[ligne_pivot])): 
        tableau[ligne_pivot][j] /= valeur_pivot 

# Vérifie si les contraintes sont de type supérieur ou égal et transforme en forme canonique
def transformer_en_forme_canonique(c, A, b):
    for i in range(len(b)): 
        if b[i] < 0:  
            b[i] = -b[i]  
            for j in range(len(A[i])):  
                A[i][j] = -A[i][j]  # Change le signe des coefficients
    return c, A, b  

# Génère des données aléatoires pour un problème d'optimisation linéaire et les écrit dans un fichier texte
def generer_donnees_aleatoires(nom_fichier, nb_variables, nb_contraintes):
    type_optimisation = random.choice(['Max', 'Min'])  
    with open(nom_fichier, 'w') as file:
        file.write(type_optimisation + '\n') 
        c = [random.randint(-10, 10) for _ in range(nb_variables)]  # Génère les coefficients de la fonction objectif
        A = [[random.randint(-10, 10) for _ in range(nb_variables)] for _ in range(nb_contraintes)]  
        b = [random.randint(10, 50) for _ in range(nb_contraintes)]  # Génère les termes constants des contraintes

        # Écriture des coefficients de la fonction objectif dans le fichier
        file.write(' '.join(map(str, c)) + '\n')
        # Écriture des coefficients des contraintes dans le fichier
        for row in A:
            file.write(' '.join(map(str, row)) + '\n')
        # Écriture des termes constants des contraintes dans le fichier
        file.write(' '.join(map(str, b)) + '\n')

    return nom_fichier  # Renvoie le nom du fichier où les données ont été écrites
