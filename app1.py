from flask import Flask, render_template
from models import Calculatrice

app = Flask(__name__)

calculatrice = Calculatrice()


@app.route("/")
def accueil():
    return render_template("index.html")