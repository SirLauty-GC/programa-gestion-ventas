import sqlite3 as sql
import var_glob

class Database():
    def __init__(self):
        try:
            self.conn = sql.connect(f"./{var_glob.archivo_guardado_actual}.db")
            self.cursor = self.conn.cursor()

            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS clientes (
                    boleta TEXT PRIMARY KEY,
                    cliente TEXT,
                    numero TEXT,
                    direccion TEXT,
                    precio INTEGER,
                    tiempo TEXT,
                    detalle TEXT
                )"""
            )

            self.conn.commit()

        except Exception as e:
            print(f"Error al conectar la base de datos: {e}")

    def cargar_datos(self):
        try:
            with sql.connect(f"./{var_glob.archivo_guardado_actual}.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM clientes")
                datos = cursor.fetchall()
                return datos
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return []

    def guardar_datos(self, boleta, nombre, numero, direccion, precio, tiempo, detalle):
        try:
            with sql.connect(f"./{var_glob.archivo_guardado_actual}.db") as conn:
                cursor = conn.cursor()
                cursor.execute(f"INSERT OR REPLACE INTO clientes VALUES('{boleta}','{nombre}', '{numero}', '{direccion}', {precio}, '{tiempo}', '{detalle}')")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def eliminar_datos(self, boleta):
        try:
            with sql.connect(f"./{var_glob.archivo_guardado_actual}.db") as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM clientes WHERE boleta=?", (boleta))
        except Exception as e:
            print(f"Error al eliminar datos: {e}")