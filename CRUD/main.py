from flask import Flask, render_template

from util import initiate_database


app = Flask(__name__)


@app.route('/')
def index():
    context = {
        
    }
    return render_template("index.html", context=context)

@app.route('/leito')
def leito():
    context = {
        
    }
    return render_template("leito.html", context=context)

@app.route('/paciente')
def paciente():
    context = {
        
    }
    return render_template("paciente.html", context=context)

@app.route('/visitante')
def visitante():
    context = {
        
    }
    return render_template("visitante.html", context=context)


if __name__ == "__main__":
    initiate_database()
    app.run(debug=True,host="0.0.0.0")
