from flask import Flask, render_template
from flaskext.mysql import MySQL

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
