#checkeo de libreria necesaria
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *

#configuracion de la pantalla
root = tk.Tk()
root.config(width=800, height=600)
root.title("Estructuras Algebraicas")
root.mainloop()


