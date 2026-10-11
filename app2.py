from flask import Flask, render_template, request
from models import Calculatrice

app = Flask(__name__)

calculatrice = Calculatrice()


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/calcul", methods=["GET", "POST"])
def calcul():
    resultat = None
    erreur = None

    if request.method == "POST":
        try:
            a = float(request.form["nombre1"])
            b = float(request.form["nombre2"])
            operation = request.form["operation"]

            if operation == "+":
                resultat = calculatrice.addition(a, b)

            elif operation == "-":
                resultat = calculatrice.soustraction(a, b)
                   elif operation == "*":
                resultat = calculatrice.multiplication(a, b)

            elif operation == "/":
                resultat = calculatrice.division(a, b)

            else:
                erreur = "Opération non reconnue."

        except ValueError as e:
            erreur = str(e)

        except (KeyError, TypeError):
            erreur = "Veuillez remplir correctement tous les champs."

    return render_template(
        "calcul.html",
        resultat=resultat,
        erreur=erreur
    )


@app.route("/historique")
def historique():
    historique_calculs = calculatrice.obtenir_historique()

    return render_template(
        "historique.html",
        historique=historique_calculs
    )
if __name__ == "__main__":
    app.run(debug=True)