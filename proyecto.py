#checkeo de libreria necesaria
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *

def accionBoton():
    print("Botoncito dandola")

class UI(tk.Frame):
    #Docstring

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        #Widgets de la UI
        self.parent.title("Estructuras Algebraicas")

        #widget label
        etiqueta = tk.Label(self.parent, text="Ejemplo simple de Label")
        etiqueta.pack()
        #widget boton
        boton = tk.Button(ROOT, text="esto es un boton", command=accionBoton)
        boton.pack()
        #widget text area
        textArea = tk.Entry(ROOT)
        textArea.pack()
        textArea.insert(0, "marselo")
        textArea.get()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()


