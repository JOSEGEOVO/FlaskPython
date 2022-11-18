import mysql.connector
from mysql.connector import Error

class dbConnection:

    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='partial',
                                                  user='root',
                                                  password='Leon12621')

    def searchRecords(self):
        query = "SELECT * FROM EquiposFutbol"
        print(query)
        cur = self.connection.cursor()
        cur.execute(query)
        # for row in cur:
        #     print(row)
        return cur

    def insertRecord(self,data):
        query = "INSERT INTO EquiposFutbol VALUES (null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(data.clave, data.nombre, data.eslogan, data.tecnico, data.pais, data.ciudad, data.categoria, data.numGoles, data.numPartidosJugados, data.numPartidosGanados, data.numCampeonatos,data.numExpulsiones, data.numEmpates )
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print('Record created successfully')

    def deleteRecord(self, recordId):
        try:
            query = "DELETE FROM EquiposFutbol WHERE id = {}".format(recordId)
            print(query)
            cur = self.connection.cursor()
            cur.execute(query)
            self.connection.commit()
            print(cur)
            print("Record delete successfully")
        except Error:
            print(Error)

    def updateRecord(self, data):
        query = "UPDATE EquiposFutbol SET clave = '{}', nombre = '{}', eslogan = '{}', tecnico = '{}', pais = '{}', ciudad = '{}', categoria = '{}', numGoles = '{}', numPartidosJugados = '{}', numPartidosGanados = '{}',numCampeonatos = '{}', numExpulsiones ='{}', numEmpates = '{}' WHERE id = '{}'".format(data.clave, data.nombre, data.eslogan, data.tecnico, data.pais, data.ciudad, data.categoria, data.numGoles, data.numPartidosJugados, data.numPartidosGanados, data.numCampeonatos,data.numExpulsiones, data.numEmpates, data.id )
        print(query, 'data')
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
