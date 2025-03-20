from tkinter import Tk, Listbox, Button
from tkinter import ttk
import var_glob

class Main():
    def __init__(self):
        self.fuente_de_texto_berlin_sans_fb = ("Berlin Sans FB", 20)
        self.root = Tk()
        self.root.geometry(var_glob.ventana_tamaño)
        self.ventana = ttk.Frame(self.root)
        self.ventana.grid()

        self.elementos_de_la_ventana()
        self.root.mainloop()
    
    def elementos_de_la_ventana(self):
        self.elemento_tabla_de_datos()
        self.elemento_boton_ingresar()

    def elemento_tabla_de_datos(self):
        self.tabla_principal = Listbox(self.ventana,
                                       bg= "#202020",
                                       fg="#FFFFFF",
                                       font=self.fuente_de_texto_berlin_sans_fb)
        self.tabla_principal.pack()
        self.tabla_principal.insert(1, "Pizza")

    def elemento_boton_ingresar(self):
        boton_ingresar = Button(self.ventana,bg="#2F71D5", text="Ingresar", command= self.comando_ingresar)
        boton_ingresar.pack()

    def comando_ingresar(self):
        print(self.tabla_principal.get(self.tabla_principal.curselection()))

if __name__ == "__main__":
    programa = Main()