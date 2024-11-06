
#Binômes : BARRY Mamadou Bailo et DIAMANKA Mamadou

from simplexe import resoudre_simplex  
from fonctions import generer_donnees_aleatoires 

# Générer des données aléatoires dans un fichier
nom_fichier = generer_donnees_aleatoires("donnees.txt", 3, 3)  # Génère des données aléatoires et les écrit dans 
    #un fichier nommé "donnees.txt" avec 3 variables et 3 contraintes est utilisé
with open(nom_fichier, "r") as file: 
    lines = file.readlines()  # Lit toutes les lignes du fichier et les stocke dans une liste

type_optimisation = lines[0].strip()  # Type d'optimisation (minimisation ou maximisation)
c = list(map(int, lines[1].strip().split()))  # Coefficients de la fonction objectif
A = [list(map(int, line.strip().split())) for line in lines[2:-1]]  # Matrice des contraintes
b = list(map(int, lines[-1].strip().split()))
resoudre_simplex(c, A, b, type_optimisation)  