class Calculatrice:
    def __init__(self):
        self._historique = []

    def addition(self, a, b):
        resultat = a + b
        self._historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def soustraction(self, a, b):
        resultat = a - b
        self._historique.append(f"{a} - {b} = {resultat}")
        return resultat

    def multiplication(self, a, b):
        resultat = a * b
        self._historique.append(f"{a} * {b} = {resultat}")
        return resultat

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro impossible.")

        resultat = a / b
        self._historique.append(f"{a} / {b} = {resultat}")
        return resultat

    def obtenir_historique(self):
        return self._historique.copy()