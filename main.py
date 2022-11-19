from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/oquefazemos")
def oquefazemos():
    return render_template("oquefazemos.html")

@app.route("/nossaspublicacoes")
def nossaspublicacoes():
    return render_template("nossaspublicacoes.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/faleconosco")
def faleconosco():
    return render_template("faleconosco.html")

# ---------- posts --------------

@app.route("/nossaspublicacoes/2")
def post_2():
    post_id = "2"
    response = make_response(render_template("post_page.html", post=post_id))
    return response

@app.route("/nossaspublicacoes/1")
def post_1():
    post_id = "1"
    response = make_response(render_template("post_page.html", post=post_id))
    return response

if __name__ == '__main__':
    app.run(use_reloader=True)

