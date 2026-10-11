from flask import Flask, jsonify, render_template, request

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


@app.route("/api/v1/calculer", methods=["POST"])
def api_calculer():
    donnees = request.get_json(silent=True)

    if not isinstance(donnees, dict):
        return jsonify({
            "erreur": "Le corps de la requête doit être un objet JSON."
        }), 400

    try:
        a = float(donnees["nombre1"])
        b = float(donnees["nombre2"])
        operation = donnees["operation"]

        operations = {
            "+": calculatrice.addition,
            "-": calculatrice.soustraction,
            "*": calculatrice.multiplication,
            "/": calculatrice.division,
        }
        if operation not in operations:
            return jsonify({"erreur": "Opération non reconnue."}), 400
        if operation == "/" and b == 0:
            return jsonify({"erreur": "La division par zéro est impossible."}), 400

        resultat = operations[operation](a, b)
        return jsonify({
            "nombre1": a,
            "nombre2": b,
            "operation": operation,
            "resultat": resultat,
        }), 200
    except (KeyError, TypeError, ValueError) as exc:
        message = str(exc) or "Données manquantes ou invalides."
        return jsonify({"erreur": message}), 400


if __name__ == "__main__":
    app.run(debug=True)
