from tkinter import Tk, Button, Entry, END
from tkinter import ttk
from database import Database
import var_glob

class Main():
    def __init__(self):
        self.database = Database()
        self.fuente_berlin_sans_fb_10 = ("Berlin Sans FB", 10)
        self.fuente_berlin_sans_fb_20 = ("Berlin Sans FB", 20)
        self.root = Tk()
        self.root.geometry(var_glob.ventana_tamaño)
        self.ventana = ttk.Frame(self.root)
        self.ventana.pack(fill="both", expand=True)

        self.elementos_de_la_ventana()
        self.root.mainloop()
    
    def elementos_de_la_ventana(self):
        self.elemento_campo_de_texto_ingresar()
        self.elemento_boton_ingresar()
        self.elemento_boton_borrar()
        self.elemento_tabla_de_datos()

    # Elementos, botones y campos
    def elemento_tabla_de_datos(self):
        columnas = ("Boleta", "Nombre", "Número", "Dirección", "Precio", "Tiempo", "Detalle")

        self.tabla_principal = ttk.Treeview(self.ventana, columns= columnas, show="headings")
        for col in columnas: # Encabezado
            self.tabla_principal.heading(col, text=col)
            self.tabla_principal.column(col, width=100)

        datos = self.database.cargar_datos()
        for fila in datos:
            self.tabla_principal.insert("", END, values=fila)
        self.tabla_principal.pack()
        
    def elemento_boton_ingresar(self):
        boton_ingresar = Button(self.ventana,bg="#2F71D5", text="Ingresar", command= self.comando_ingresar, font=self.fuente_berlin_sans_fb_10)
        boton_ingresar.pack()
        
    def elemento_boton_borrar(self):
        boton_borrar = Button(self.ventana,bg="#2F71D5", text="Borrar", command= self.comando_borrar, font=self.fuente_berlin_sans_fb_10)
        boton_borrar.pack()

    def elemento_campo_de_texto_ingresar(self):
        self.campo_de_texto_ingresar = Entry(self.ventana)
        self.campo_de_texto_ingresar.pack()

    # Comandos a ejeutar
    def comando_ingresar(self):
        nuevo_id = len(self.tabla_principal.get_children()) + 1
        nuevo_nombre = self.campo_de_texto_ingresar.get()
        # Llamar a la base de datos y pasarle: boleta, nombre, numero, direccion, precio, tiempo, detalle
        if nuevo_nombre:
            self.tabla_principal.insert("", END, values=(nuevo_id, nuevo_nombre, "N/A"))
            self.database.guardar_datos(nuevo_id, nuevo_nombre, "N/A","",1,2,"")
        else:
            print("ingresá nombre")

    def comando_borrar(self):
        fila_seleccionada = self.tabla_principal.selection()
        fila_en_database = self.tabla_principal.item(fila_seleccionada, "values") 
    
        if fila_seleccionada:
            self.tabla_principal.delete(fila_seleccionada)
            self.database.eliminar_datos(fila_en_database[0])

if __name__ == "__main__":
    programa = Main()