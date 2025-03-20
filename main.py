from tkinter import Tk, Listbox, Button, Entry, END
from tkinter import ttk
import var_glob

class Main():
    def __init__(self):
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
        columnas = ("ID", "Nombre", "Valor")

        self.tabla_principal = ttk.Treeview(self.ventana, columns= columnas, show="headings")
        for col in columnas: # Encabezado
            self.tabla_principal.heading(col, text=col)
            self.tabla_principal.column(col, width=100)

        datos = [(1,"Nombre 1", 17),(2,"Nombre 2", 17)]
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
        self.tabla_principal.insert("", END, values=(nuevo_id, nuevo_nombre, "N/A"))

    def comando_borrar(self):
        fila_seleccionada = self.tabla_principal.selection()
        if fila_seleccionada:
            self.tabla_principal.delete(fila_seleccionada)

if __name__ == "__main__":
    programa = Main()