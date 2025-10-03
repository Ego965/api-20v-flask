import sqlite3

DATABASE_NAME = "database.db"

def get_db_connection():
    """
    Establece y devuelve una conexión a la base de datos.
    Asegura que las filas se devuelvan como diccionarios (sqlite3.Row).
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn