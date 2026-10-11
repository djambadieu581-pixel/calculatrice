from models import Calculatrice

calculatrice = Calculatrice()

print("Addition :", calculatrice.addition(10, 5))
print("Soustraction :", calculatrice.soustraction(10, 5))
print("Multiplication :", calculatrice.multiplication(10, 5))
print("Division :", calculatrice.division(10, 5))

print("Historique :", calculatrice.obtenir_historique())