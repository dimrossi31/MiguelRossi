from flask import Flask, render_template

app = Flask(__name__)

# Rota para a homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Rota para a página de músicas
@app.route("/Musicas")
def musicas():
    return render_template("Musicas.html")

# Rota para a cifra da música Bondade de Deus
@app.route("/Musicas/BondadeDeDeus")
def bondade_de_deus():
    return render_template("bondade_de_deus.html")

# Rota para a cifra da música Boa Parte
@app.route("/Musicas/BoaParte")
def boa_parte():
    return render_template("boa_parte.html")

# Rota para a cifra da música Rompendo em Fé
@app.route("/Musicas/RompendoEmFe")
def rompendo_em_fe():
    return render_template("rompendo_em_fe.html")

# Rota para a cifra da música Te Agradeço
@app.route("/Musicas/TeAgradeco")
def te_agradeco():
    return render_template("te_agradeco.html")

if __name__ == "__main__":
    app.run(debug=True)
