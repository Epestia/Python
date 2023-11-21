class Calculatrice:
    def __init__(self):
        pass

    def addition(self, nbr1, nbr2):
        return nbr1 + nbr2

# Créer une instance de la classe Calculatrice
calculatrice = Calculatrice()

# Demander à l'utilisateur d'entrer deux nombres
nbr1 = float(input("Entrez nombre1 : "))
nbr2 = float(input("Entrez nombre2 : "))

# Appeler la méthode addition de l'instance de la calculatrice
resultat = calculatrice.addition(nbr1, nbr2)

# Afficher le résultat de l'addition
print("Le résultat de l'addition est :", resultat)
