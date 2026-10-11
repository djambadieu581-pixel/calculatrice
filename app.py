from flask import Flask, redirect, render_template, request, url_for

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
            operations = {
                "addition": calculatrice.addition,
                "soustraction": calculatrice.soustraction,
                "multiplication": calculatrice.multiplication,
                "division": calculatrice.division,
            }
            if operation not in operations:
                raise ValueError("Choisissez une opération valide.")
            resultat = operations[operation](a, b)
        except (KeyError, ValueError) as exc:
            erreur = str(exc) or "Veuillez saisir deux nombres valides."

    return render_template("calcul.html", resultat=resultat, erreur=erreur)


@app.route("/historique")
def historique():
    return render_template("historique.html", historique=calculatrice.obtenir_historique())


if __name__ == "__main__":
    app.run(debug=True)
