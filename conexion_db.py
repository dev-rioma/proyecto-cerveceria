from logging import exception
import sqlite3

def conexion():
    try:
        conxiondb = sqlite3.connect("database/bd_cerveceria.db")
        print("Conexion Exitosa")
        cursor = conxiondb.cursor()
        return cursor
    except exception as ex:
        print(ex)
        
def consulta():
    cursor = (conexion())
    rows=cursor.execute("SELECT clave from login")
    for row in rows:
        print(row)


consulta()