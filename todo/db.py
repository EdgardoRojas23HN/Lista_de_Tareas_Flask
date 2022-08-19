import mysql.connector

import click 

from flask import current_app, g
from flask.cli import with_appcontext  #Nos servira para el contexto de nuestr app
from .schema import instructions

def get_db():
    if 'db' not in g: #Con esta funcion llamamos la base de datos
        g.db = mysql.connector.connect(
            host=current_app.config['DATBASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary = True) #Con esta funcion llamamos el cursor
        return g.db, g.c

def close_db(e=None):
    db= g.pop('db', None)

    if db is not None:
        db.close()

def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')        

def init_app(app): #Cerramos la conexion
    app.teardown_appcontext(close_db)