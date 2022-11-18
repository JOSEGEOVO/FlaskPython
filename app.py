from flask import Flask, render_template, request, redirect, url_for
from util import dbConnection
from models.footTeam import footballTeam


app = Flask(__name__)


@app.route('/')
def index():
    mysqlController = dbConnection()
    records = mysqlController.searchRecords()
    return render_template('index.html', records=records)


@app.route('/handleRecord', methods=(['POST']))
def handleRecord():

    football = footballTeam()
    mysqlController = dbConnection()

    if request.form['action'] == 'delete':
        football.clave = request.form['clave']
        football.nombre =request.form['nombre']
        football.eslogan= request.form['eslogan']
        football.tecnico = request.form['tecnico']
        football.pais = request.form['pais']
        football.ciudad = request.form['ciudad']
        football.categoria = request.form['categoria']
        football.numGoles= request.form['numGoles']
        football.numPartidosJugados = request.form['numPartidosJugados']
        football.numPartidosGanados = request.form['numPartidosGanados']
        football.numCampeonatos = request.form['numCampeonatos']
        football.numExpulsiones =request.form['numExpulsiones']
        football.numEmpates = request.form['numEmpates']

        
        
        mysqlController.insertRecord(football)
    else:
        football.id = request.form['idUpdate']
        football.clave = request.form['clave']
        football.nombre =request.form['nombre']
        football.eslogan= request.form['eslogan']
        football.tecnico = request.form['tecnico']
        football.pais = request.form['pais']
        football.ciudad = request.form['ciudad']
        football.categoria = request.form['categoria']
        football.numGoles= request.form['numGoles']
        football.numPartidosJugados = request.form['numPartidosJugados']
        football.numPartidosGanados = request.form['numPartidosGanados']
        football.numCampeonatos = request.form['numCampeonatos']
        football.numExpulsiones =request.form['numExpulsiones']
        football.numEmpates = request.form['numEmpates']

        mysqlController.updateRecord(football)

    return redirect(url_for('index'))

@app.route('/delete', methods=(['POST']))
def delete():

    mysqlController = dbConnection()
    mysqlController.deleteRecord(recordId=request.form['id'])

    return redirect(url_for('index'))

# @app.route('/api', methods=(['GET']))
# def apiRequest():
#     try:
#         URL = "https://jsonplaceholder.typicode.com/posts"
#         r = requests.get(url=URL)
#         data = r.json()
#         return data
#     except requests.exceptions.HTTPError as err:
#         raise SystemExit(err)


# @app.route('/handleRecord', methods=(['POST']))
# def handleRecord():
#     if request.form['action'] == 'delete':
#         databaseController.deleteRecord({'_id': ObjectId(request.form['id'])})
#     else:
#         filter = {'_id': ObjectId(request.form['id'])}
#         dataToUpdate = {"$set": {
#             'email': request.form['email'], 'password': request.form['password']}}
#         databaseController.update(filter, dataToUpdate)

#     return redirect(url_for('index'))


app.run(debug=True)
