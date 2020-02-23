#checkeo de libreria necesaria
try:
    import tkinter as tk

except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *
import winsound
import pygame


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

        #label principal
        label1 = tk.Label(self.parent, text="Estructuras Algebraicas", width=600, height=3)
        label1.config(font=("Menlo", 13, "bold"))
        label1.pack() 
        #logo vader
        logo1 = tk.Label(self.parent, image=img)
        logo1.place(x=20, y=8)
        logo2 = tk.Label(self.parent, image=img)
        logo2.place(x=730, y=8)
        #label datos
        label2 = tk.Label(self.parent, text="Introduzca aqui las expresiones a checkear")
        label2.config(font=("Menlo", 11, "bold"))
        label2.place(x=18, y=100)
        #label ecuacion 1
        label3 = tk.Label(self.parent, text="Ecuacion 1")
        label3.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
        label3.place(x=43, y=145)
        #label ecuacion 2
        label4 = tk.Label(self.parent, text="Ecuacion 2")
        label4.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
        label4.place(x=280, y=145)
        #widget boton
        boton = tk.Button(self.parent, text="Comprobar", command=accionBoton)
        boton.config(font=("bold"))
        boton.place(x=160, y=220)
        #text area ecuacion 1
        textArea1 = tk.Entry(self.parent)
        textArea1.place(x=20, y=170)
        textArea1.insert(0, "")
        #text area ecuacion 2
        textArea2 = tk.Entry(self.parent)
        textArea2.place(x=255, y=170)
        textArea2.insert(0, "")

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    ROOT.resizable(width=False, height=False)
    ROOT.configure(background="#17212C")
    img = PhotoImage(file="vader.png")
    pygame.mixer.init()
    pygame.mixer.music.load("march.mp3")
    pygame.mixer.music.play()
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()


