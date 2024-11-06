from fonctions import trouver_pivot, mettre_a_jour_tableau, transformer_en_forme_canonique

# Algorithme du simplexe pour résoudre le problème d'optimisation linéaire
def simplex(tableau):
    iteration = 1 
    while True: 
        print(f"Iteration {iteration}:") 
        for ligne in tableau: 
            print(ligne)
        colonne_pivot = trouver_pivot(tableau)  # Recherche de la colonne du pivot
        if colonne_pivot is None:  
            break 

        # Recherche de la ligne du pivot
        ligne_pivot = None
        ratio_min = float('inf') 
        for i in range(len(tableau) - 1):  
            if tableau[i][colonne_pivot] > 0:  
                ratio = tableau[i][-1] / tableau[i][colonne_pivot]  # Calcul du ratio
                if ratio < ratio_min:  
                    ratio_min = ratio  # Mettre à jour le ratio minimum
                    ligne_pivot = i  # Mettre à jour la ligne pivot

        if ligne_pivot is None:  # Si aucune ligne pivot n'est trouvée
            print("Erreur: Pas de ligne pivot trouvée.")  
            break

        valeur_pivot = tableau[ligne_pivot][colonne_pivot]  # Valeur du pivot
        print(f"Pivot: {valeur_pivot}")  # Affichage de la valeur du pivot
        print(f"Emplacement du pivot: Ligne: {ligne_pivot}, Colonne: {colonne_pivot}")  # Affichage de l'emplacement du pivot

        mettre_a_jour_tableau(tableau, ligne_pivot, colonne_pivot, valeur_pivot)
        iteration += 1  

# Fonction pour résoudre le problème d'optimisation linéaire en utilisant l'algorithme du simplexe
def resoudre_simplex(c, A, b, type_optimisation):
    # Transformation en forme canonique si nécessaire
    c, A, b = transformer_en_forme_canonique(c, A, b)
    tableau = [ligne[:] + [val] for ligne, val in zip(A, b)]  # Crée une copie des contraintes et ajoute les termes constants
    if type_optimisation == 'Min':
        c = [-val for val in c]  # Pour un problème de minimisation, inverser les coefficients de c
    tableau.append(c + [0])  # Ajoute la ligne de la fonction objectif au tableau

    print("Tableau initial:") 
    for ligne in tableau:
        print(ligne)
    simplex(tableau)  # Appel à la fonction du simplexe pour résoudre le problème

    print("Tableau final:")  # Affichage du tableau final
    for ligne in tableau:
        print(ligne)
    # Récupération des solutions optimales des variables de décision
    solutions = [0] * len(c)  
    for i in range(len(A)):  
        for j in range(len(c)): 
            if tableau[i][j] == 1 and tableau[i][-1] >= 0:  
                solutions[j] = tableau[i][-1]  

    # Calcul de la valeur optimale de la fonction objectif
    valeur_objective = tableau[-1][-1]  # Récupération de la valeur dans la case objectif du tableau final
    if type_optimisation == 'Min':  
        valeur_objective = -valeur_objective  # Inversion de la valeur

    # Affichage des résultats
    print(f"Solutions optimales des variables de décision: {solutions}") 
    print(f"Valeur optimale de la fonction objectif ({type_optimisation}): {valeur_objective}") 

    return solutions, valeur_objective  
