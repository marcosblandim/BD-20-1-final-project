from flask import Flask, render_template, url_for
from flaskext.mysql import MySQL
import os

from util import initiate_database


app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'PROJETO_COVID'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# conn = mysql.connect()
# cursor = conn.cursor()

# a = cursor.execute("select * from LEITO;")
# print(cursor.fetchall())

# conn.commit()
# cursor.close() 
# conn.close()


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

@app.route('/')
def index():
    context = {

    }
    return render_template("index.html", context=context)

@app.route('/leito')
def leito():

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
