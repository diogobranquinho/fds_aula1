from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Bom, bonito e barato</p>"

@app.route("/sobre")
def sobre():
    return "<h1> Portal de vendas de coisas novas e usadas</h1>"

@app.route("/sobre/privacidade")
def privacidade():
    return "<h4> Privacidade nao existe neste site</h4>"