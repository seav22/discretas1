#checkeo de libreria necesaria
try:
    import tkinter as tk

except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *
import pygame
from tkinter.ttk import *

def botonComprobar():
    print("Esta es la ecuacion 1: " + textArea1.get())
    print("Esta es la ecuacion 2: " + textArea2.get())

'''<CONFIGURACION DEL WINDOWS>'''
#Inicializo la pantalla y configuro propiedades como su tamaño y color de fondo.
ROOT = tk.Tk()
ROOT.title("Estructuras Algebraicas")
ROOT.geometry("800x650")
ROOT.resizable(width=False, height=False)
ROOT.configure(background="#17212C")
img = PhotoImage(file="vader.png")
pygame.mixer.init()
pygame.mixer.music.load("march.mp3")
pygame.mixer.music.play()
v = ""
'''</CONFIGURACION DEL WINDOWS>'''

'''<WIDGETS>'''
#label principal
label1 = tk.Label(ROOT, text="Estructuras Algebraicas", width=600, height=3)
label1.config(font=("Menlo", 13, "bold"))
label1.pack() 
#logo vader
logo1 = tk.Label(ROOT, image=img)
logo1.place(x=20, y=8)
logo2 = tk.Label(ROOT, image=img)
logo2.place(x=730, y=8)
#label datos
label2 = tk.Label(ROOT, text="Introduzca aqui las expresiones a checkear")
label2.config(font=("Menlo", 11, "bold"))
label2.place(x=18, y=90)
#label intrucciones
label3 = tk.Label(ROOT, text="INTRUCCIONES:")
label3.config(font=("Menlo", 11, "bold"))
label3.place(x=575, y=90)
#label cojunto numerico
labeln = tk.Label(ROOT, text="Seleccione un conjunto numerico:")
labeln.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
labeln.place(x=110, y=130)
#Text widget para instrucciones
instrucciones = tk.Text(ROOT, height=30, width=40)
instrucciones.config(font=("Menlo", 9), fg="#FFFFFF", bg="#17212C", borderwidth=0)
instrucciones.place(x=500, y=140)
instrucciones.insert(tk.END, '1)Seleccione el conjunto numerico\n\n2)Introduzca las ecuaciones\n\n3)Presione le boton de comprobar\n\n4)Las comprobaciones seran mostradas\n en el cuadro inferior')
instrucciones.config(state=DISABLED)
#label integrantes
integrantes = tk.Label(ROOT, text="Sebastian Avendaño, V-26765567.\nSebastian Alvarez V-xxxxxxxx")
integrantes.place(x=550, y=550)
#label ecuacion 1
label4 = tk.Label(ROOT, text="Ecuacion 1")
label4.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
label4.place(x=63, y=215)
#label ecuacion 2
label5 = tk.Label(ROOT, text="Ecuacion 2")
label5.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
label5.place(x=300, y=215)
#text area ecuacion 1
textArea1 = tk.Entry(ROOT)
textArea1.place(x=40, y=240)
textArea1.insert(0, "")
#text area ecuacion 2
textArea2 = tk.Entry(ROOT)
textArea2.place(x=275, y=240)
textArea2.insert(0, "")
#widget boton
boton = tk.Button(ROOT, text="Comprobar", command=botonComprobar)
boton.config(font=("bold"))
boton.place(x=170, y=280)
#radio buttons
radio1 = tk.Radiobutton(ROOT, text="NATURALES", variable=v, value=1)
radio1.place(x=20, y=160)
radio2 = tk.Radiobutton(ROOT, text="ENTEROS", variable=v, value=2)
radio2.place(x=120, y=160)
radio3 = tk.Radiobutton(ROOT, text="REALES", variable=v, value=3)
radio3.place(x=220, y=160)
radio4 = tk.Radiobutton(ROOT, text="COMPLEJOS", variable=v, value=4)
radio4.place(x=320, y=160)
#separator
separador1 = Separator(ROOT, orient=VERTICAL).place(x=480, y=80, height=500)
separador2 = Separator(ROOT, orient=HORIZONTAL).place(x=45, y=340, width=390)
#scrollbar
scroll = Scrollbar(ROOT)
scroll.place(x = 428, y = 385, height=200)
#Text widget para resultado de comprobaciones
resultado = tk.Text(ROOT, height=17, width=50)
resultado.config(font=("Menlo", 9), fg="#FFFFFF", bg="#31475e", borderwidth=4, relief=SUNKEN)
resultado.place(x=65, y=365)
resultado.insert(tk.END, "a")
resultado.config(state=DISABLED)
#test
scroll.config(command=resultado.yview)

'''</WIDGETS>'''

#Main loop y destruccion de ventana
ROOT.mainloop()
ROOT.destroy()




        

    


