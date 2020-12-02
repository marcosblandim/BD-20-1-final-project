from flask import Flask, render_template, url_for, request, redirect, flash
from flaskext.mysql import MySQL
import os
import pymysql

import util


app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'PROJETO_COVID'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = b'97643917912516513155'
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

    conn = mysql.connect()
    cursor = conn.cursor()

    num_pacientes = cursor.execute("select * from PACIENTE;")
    pacientes = cursor.fetchall()

    cursor.execute("select * from LEITO;")
    leitos = cursor.fetchall()
    
    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "pacientes": pacientes,
        "num_pacientes": num_pacientes,
        "leitos": leitos
    }

    return render_template("paciente.html", context=context)


@app.route('/visitante', methods=("GET",))
def visitante():

    conn = mysql.connect()
    cursor = conn.cursor()

    num_visitantes = cursor.execute("select * from VISITANTE;")
    visitantes = cursor.fetchall()
    
    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "visitantes": visitantes,
        "num_visitantes": num_visitantes
    }
    return render_template("visitante.html", context=context)


@app.route('/visita', methods=("GET",))
def visita():

    conn = mysql.connect()
    cursor = conn.cursor()

    num_visitas = cursor.execute("select * from VISITAS;")
    visitas = cursor.fetchall()
    
    cursor.execute("select CPF, NOME from PACIENTE;")
    pacientes = cursor.fetchall()

    cursor.execute("select CPF, NOME from VISITANTE;")
    visitantes = cursor.fetchall()

    conn.commit()
    cursor.close() 
    conn.close()

    context = {
        "visitas": visitas,
        "num_visitas": num_visitas,
        "pacientes": pacientes,
        "visitantes": visitantes
    }
    return render_template("visita.html", context=context)


@app.route('/leito/create', methods=("POST",))
def create_leito():
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO LEITO VALUES ({0},{1},{2},{3},{4})".format(*request.form.values()))
    except pymysql.err.IntegrityError:
        flash('Leito já existe', 'error')
        return redirect(url_for('leito'))

    conn.commit()
    cursor.close() 
    conn.close()
    flash('Leito registrado com sucesso', 'success')
    return redirect(url_for('leito'))


@app.route('/leito/update', methods=("GET","POST"))
def update_leito():
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == "GET":        
        cursor.execute("SELECT * FROM LEITO WHERE NUMERO={0} AND ID_HOSPITAL={1};".format(*request.args.values()))
        leitos = cursor.fetchall()

        conn.commit()
        cursor.close() 
        conn.close()

        context = {
            "leito": leitos[0],
        }
        return render_template("update_leito.html", context=context)

    form = request.form
    cursor.execute("""
        UPDATE LEITO 
        SET ANDAR={2}, CAPACIDADE={3}, INTERNADOS={4}
        WHERE NUMERO={0} AND ID_HOSPITAL={1};
        """.format(*form.values())
    )

    conn.commit()
    cursor.close() 
    conn.close()

    return redirect(url_for('leito'))


@app.route('/leito/delete', methods=("GET",))
def delete_leito():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM LEITO WHERE NUMERO={0} AND ID_HOSPITAL={1};".format(*request.args.values()))
    
    conn.commit()
    conn.close()
    return redirect(url_for('leito'))


@app.route('/paciente/create', methods=("POST",))
def create_paciente():
    conn = mysql.connect()
    cursor = conn.cursor()

    form = list(request.form.values())
    leito = form.pop()
    leito = leito.split()
    form += leito
    formValues = [value or None for value in form]

    try:
        # cursor.execute('INSERT INTO PACIENTE VALUES ("{0}","{1}",{2},"{3}","{4}","{5}",{6},{7})'.format(*form))
        cursor.execute('INSERT INTO PACIENTE VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (formValues))
    except pymysql.err.IntegrityError:
        flash('Paciente já existe', 'error')
        return redirect(url_for('paciente'))

    conn.commit()
    cursor.close() 
    conn.close()
    flash('PACIENTE registrado com sucesso', 'success')
    return redirect(url_for('paciente'))


@app.route('/paciente/update', methods=("GET","POST"))
def update_paciente():
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == "GET":        
        cursor.execute("SELECT * FROM PACIENTE WHERE CPF='{0}';".format(*request.args.values()))
        pacientes = cursor.fetchall()

        cursor.execute("select * from LEITO;")
        leitos = cursor.fetchall()

        conn.commit()
        cursor.close() 
        conn.close()

        context = {
            "paciente": pacientes[0],
            "leitos": leitos
        }
        return render_template("update_paciente.html", context=context)

    form = list(request.form.values())
    leito = form.pop()
    leito = leito.split()
    form += leito

    # cursor.execute("""
    #     UPDATE PACIENTE 
    #     SET NOME="{1}", ESTADO_SAUDE={2}, DATA_NASC="{3}", DATA_INICIO="{4}", DATA_FIM="{5}", ID_HOSPITAL={6}, NUMERO={7}
    #     WHERE CPF="{0}";
    #     """.format(*form)
    # )

    # formValues = [value or None for value in request.form.values()]
    formValues = [value or None for value in form]
    cursor.execute( """UPDATE PACIENTE
        SET NOME=%s, ESTADO_SAUDE=%s, DATA_NASC=%s, DATA_INICIO=%s, DATA_FIM=%s, ID_HOSPITAL=%s, NUMERO=%s
        WHERE CPF=%s;
        """, (*formValues[1:], formValues[0])
    )

    conn.commit()
    cursor.close() 
    conn.close()

    return redirect(url_for('paciente'))


@app.route('/paciente/delete', methods=("GET",))
def delete_paciente():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM PACIENTE WHERE CPF="{0}";'.format(*request.args.values()))
    
    conn.commit()
    conn.close()
    return redirect(url_for('paciente'))


@app.route('/visitante/create', methods=("POST",))
def create_visitante():
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO VISITANTE VALUES ("{0}","{1}",{2},"{3}")'.format(*request.form.values()))
    except pymysql.err.IntegrityError:
        flash('Visitante já existe', 'error')
        return redirect(url_for('visitante'))

    conn.commit()
    cursor.close() 
    conn.close()
    flash('Visitante registrado com sucesso', 'success')
    return redirect(url_for('visitante'))


@app.route('/visitante/update', methods=("GET","POST"))
def update_visitante():
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == "GET":        
        cursor.execute('SELECT * FROM VISITANTE WHERE CPF="{0}";'.format(*request.args.values()))
        visitantes = cursor.fetchall()

        conn.commit()
        cursor.close() 
        conn.close()

        context = {
            "visitante": visitantes[0],
        }
        return render_template("update_visitante.html", context=context)

    form = request.form
    cursor.execute("""
        UPDATE VISITANTE 
        SET NOME="{1}", ESTADO_SAUDE={2}, DATA_NASC="{3}"
        WHERE CPF="{0}";
        """.format(*form.values())
    )

    conn.commit()
    cursor.close() 
    conn.close()

    return redirect(url_for('visitante'))

@app.route('/visitante/delete', methods=("GET",))
def delete_visitante():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM VISITANTE WHERE CPF="{0}"'.format(*request.args.values()))
    
    conn.commit()
    conn.close()
    return redirect(url_for('visitante'))


@app.route('/visita/create', methods=("POST",))
def create_visita():
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO VISITAS VALUES ("{0}","{1}","{2}")'.format(*request.form.values()))
    except pymysql.err.IntegrityError:
        flash('Visita já existe', 'error')
        return redirect(url_for('visita'))

    conn.commit()
    cursor.close() 
    conn.close()
    flash('Visita registrada com sucesso', 'success')
    return redirect(url_for('visita'))


@app.route('/visita/delete', methods=("GET",))
def delete_visita():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM VISITAS WHERE CPF_PACIENTE="{0}" AND CPF_VISITANTE="{1}" AND DATA_VISITA="{2}";'.format(*request.args.values()))
    
    conn.commit()
    conn.close()
    return redirect(url_for('visita'))


if __name__ == "__main__":
    util.initiate_db()
    app.run(debug=True,host="0.0.0.0")
