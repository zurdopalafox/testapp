from django.db import models
import oracledb
import pymysql

# Create your models here.

class Serie:
    def __init__(self):
        self.idSerie = 0
        self.nombre =""
        self.imagen = ""
        self.anyo = 0

class Personaje:
    def __init__(self):
        self.idPersonaje = 0
        self.personaje = ""
        self.imagen = ""
        self.idSerie = 0

class ServiceSeriesOracle:
    def __init__(self):
        self.connection = oracledb.connect(user="system", password="oracle", dsn="localhost/freepdb1")

    def getSeries(self):
        cursor = self.connection.cursor()
        sql = "select * from SERIES"
        listaseries = [] 
        cursor.execute(sql)
        for fila in cursor:
            serie = Serie()
            serie.idSerie = fila[0]
            serie.nombre = fila[1]
            serie.imagen =fila[2]
            serie.anyo = fila[3]
            listaseries.append(serie)
        cursor.close()
        return listaseries
    
    def getPersonajesSerie(self, idserie):
        cursor = self.connection.cursor()
        sql = "select * from PERSONAJES where IDSERIE = :idserie"
        listapersonajes = [] 
        cursor.execute(sql,(idserie,))
        for fila in cursor:
            personaje = Personaje()
            personaje.idPersonaje = fila[0]
            personaje.personaje = fila[1]
            personaje.imagen = fila[2]
            personaje.idSerie = fila[3]
            listapersonajes.append(personaje)
        cursor.close()
        return listapersonajes
    
    def insertarPersonaje(self, id, nombre, imagen, idserie):
        cursor = self.connection.cursor()
        sql = "insert into PERSONAJES values (:id, :nombre, :imagen, :idserie)"
        cursor.execute(sql, (id, nombre, imagen, idserie,))
        self.connection.commit()
        cursor.close()    


class ServiceSeries:
    def __init__(self):
        self.connection = pymysql.connect(host="sql7.freesqldatabase.com", port=3306, user="sql7818176", password="FzMNGLTjrq", database="sql7818176")

    def getSeries(self):
        cursor = self.connection.cursor()
        sql = "select * from SERIES"
        listaseries = [] 
        cursor.execute(sql)
        for fila in cursor:
            serie = Serie()
            serie.idSerie = fila[0]
            serie.nombre = fila[1]
            serie.imagen =fila[2]
            serie.anyo = fila[3]
            listaseries.append(serie)
        cursor.close()
        return listaseries
    
    def getPersonajesSerie(self, idserie):
        cursor = self.connection.cursor()
        sql = "select * from PERSONAJES where IDSERIE = %s"
        listapersonajes = [] 
        cursor.execute(sql,(idserie,))
        for fila in cursor:
            personaje = Personaje()
            personaje.idPersonaje = fila[0]
            personaje.personaje = fila[1]
            personaje.imagen = fila[2]
            personaje.idSerie = fila[3]
            listapersonajes.append(personaje)
        cursor.close()
        return listapersonajes
    
    def insertarPersonaje(self, id, nombre, imagen, idserie):
        cursor = self.connection.cursor()
        sql = "insert into PERSONAJES values (%s, %s, %s, %s)"
        cursor.execute(sql, (id, nombre, imagen, idserie,))
        self.connection.commit()
        cursor.close()    



