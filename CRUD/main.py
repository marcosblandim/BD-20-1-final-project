from flask import Flask, render_template, url_for, request, redirect
from flaskext.mysql import MySQL
import os

from util import *


app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'PROJETO_COVID'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


##### clean the cache #####
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
##### clean the cache #####

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/leito', methods=("GET",))
def leito():
    if request.method == "POST":
        pass

    conn = mysql.connect()
    cursor = conn.cursor()

    num_leitos = cursor.execute("select * from LEITO;")
    leitos = cursor.fetchall()
    
    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "leitos": leitos,
        "num_leitos": num_leitos
    }
    return render_template("leito.html", context=context)

@app.route('/paciente', methods=("GET",))
def paciente():
    if request.method == "POST":
        pass

    conn = mysql.connect()
    cursor = conn.cursor()

    num_leitos = cursor.execute("select * from PACIENTE;")
    leitos = cursor.fetchall()
    
    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "pacientes": leitos,
        "num_pacientes": num_leitos
    }

    return render_template("paciente.html", context=context)

@app.route('/visitante', methods=("GET",))
def visitante():
    if request.method == "POST":
        pass

    conn = mysql.connect()
    cursor = conn.cursor()

    num_leitos = cursor.execute("select * from VISITANTE;")
    leitos = cursor.fetchall()
    
    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "visitantes": leitos,
        "num_visitantes": num_leitos
    }
    return render_template("visitante.html", context=context)

@app.route('/leito/update', methods=("GET",))
def update_leito():
    util.update_leito(request)
    return redirect(url_for('leito'))

@app.route('/leito/delete', methods=("GET",))
def delete_leito():
    util.delete_leito(request)
    return redirect(url_for('leito'))

@app.route('/paciente/update', methods=("GET",))
def update_paciente():
    util.update_paciente(request)
    return redirect(url_for('paciente'))

@app.route('/paciente/delete', methods=("GET",))
def delete_paciente():
    util.delete_paciente(request)
    return redirect(url_for('paciente'))
    
@app.route('/visitante/update', methods=("GET",))
def update_visitante():
    util.update_visitante(request)
    return redirect(url_for('visitante'))

@app.route('/visitante/delete', methods=("GET",))
def delete_visitante():
    util.delete_visitante(request)
    return redirect(url_for('visitante'))


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
