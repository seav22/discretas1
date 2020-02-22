#checkeo de libreria necesaria
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *

class UI(tk.Frame):
    """Docstring."""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.parent.title("Un titulo para la ventana")

        etiqueta = tk.Label(self.parent, text="Ejemplo simple de Label")
        etiqueta.pack()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("300x100")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()


