#checkeo de libreria necesaria
try:
    import tkinter as tk

except ImportError:
    raise ImportError("Se requiere la libreria tkinter para continuar")

from tkinter import *
from tkinter import messagebox
import pygame
from tkinter.ttk import *
import cmath
from math import sqrt


'''<CODIGO>'''

a = 10
b = 4
c = 7
mon = a+b
mon1 = a*b
m = 0

#Propiedades
def monoideA(e): # Funcion que demuestra existencia o no del monoide asociativo (a * b) * c = a * (b * c)  [(a * b)]
	#Reemplazando en asociativa

	aso = "(a * b)" # * c
	aso1 = "(a * c)"
	aso3 = "a * b"
	asoR = aso.replace("a * b", e) #Sustituyendo a * b por la expresión ingresada
	asoR2 = aso1.replace("a * c", e) #Sustituyendo a * c por la expresión ingresada
	asoR3 = asoR2.replace("b", "c")  #Sustituyendo b de la expresión ingresada por c
	asoR4 = asoR3.replace("a","b") #Sustituyendo a de la expresión ingresada por b
	
	#Aplicando segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	mostrar.insert(tk.END,"Procedimiento: \n")
	mostrar.insert(tk.END,"\nTenemos que: \n[",e," = a * b ]")
	mostrar.insert(tk.END,"Aplicamos la propiedad asociativa: ")
	mostrar.insert(tk.END,"En la propiedad asociativa:\n\n (a * b) * c = a * (a * c) \n")
	mostrar.insert(tk.END,"\nSe demuestra:")
	mostrar.insert(tk.END, asoR, " * c = a * ", asoR4)#primer paso: (2*a - b)  * c = a *  (2*b - c)
	mostrar.insert(tk.END,"\nPrimera igualdad: ")
	mostrar.insert(tk.END," a = ", asoR)
	mostrar.insert(tk.END," b = c")
	mostrar.insert(tk.END,"\nSegunda igualdad: ")
	mostrar.insert(tk.END," a = a")
	mostrar.insert(tk.END," b = ", asoR4)
	mostrar.insert(tk.END,"\nCon esto podemos entender que: a * b\n")

	if (resultado == resultado2):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"Queda claro que la sigiente expresión:\n  (",e,")")
		mostrar.insert(tk.END,"\nSI CUMPLE, \nse trata de un monoide asociativo")
		return "1"

	else:
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END)
		mostrar.insert(tk.END,"Ha sido demostrado que\n la siquiente expresión: (",e,")")
		mostrar.insert(tk.END,"\nNO CUMPLE, \nNO ES monoide asociativo ")

def monoideB(e):
	#aplicamos remplazo en asociativa
	aso = "(a + b)"
	aso1 = "(a + c)"
	aso3 = "a + b"
	asoR = aso.replace("a + b", e)
	asoR2 = aso1.replace("a + c", e)
	asoR3 = asoR2.replace("b", "c")
	asoR4 = asoR3.replace("a","b")
	
	#aplicamos segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	#2*(2*a - b) - c  =  2*a - (2*b - c)

	mostrar.insert(tk.END,"\nMuestra del procedimiento: \n")
	mostrar.insert(tk.END,"\nTenemos: [",e," = a + b ]")
	mostrar.insert(tk.END,"Aplicamos la \npropiedad asociativa. . . ")
	mostrar.insert(tk.END,"\n(a + b) + c = a + (a + c) \n")
	mostrar.insert(tk.END,"\nSe demuestra la propiedad: \n")
	mostrar.insert(tk.END,asoR, " + c = a + ", asoR4)#primer paso: (2*a - b)  + c = a +  (2*b - c)
	mostrar.insert(tk.END,"\nPrimera igualdad: ")
	mostrar.insert(tk.END," a = ", asoR)
	mostrar.insert(tk.END," b = c")
	mostrar.insert(tk.END,"\nSegunda igualdad: ")
	mostrar.insert(tk.END," \na = a")
	mostrar.insert(tk.END," \nb = ", asoR4)
	mostrar.insert(tk.END,"\nEs posible dar a entender que:\n a * b\n")

	if (resultado == resultado2):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\nSe demuestra que la siguiente expresión (",e,")\n")
		mostrar.insert(tk.END,"\nSI CUMPLE, ES UN monoide asociativo \n")
		mostrar.insert(tk.END,"\nResultado numérico: \n")
		mostrar.insert(tk.END,resultado," = ",resultado2)
		return "1"

	else:
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,)
		mostrar.insert(tk.END,"\nSe demuestra que la siguiente ecuacion (",e,")\n")
		mostrar.insert(tk.END,"\nNO CUMPLE, \nNO SE TRATA DE UN monoide asociativo \n")
		mostrar.insert(tk.END,resultado," = ",resultado2)

#Copia de A
def monoideC(e): # Funcion que demuestra existencia o no del monoide asociativo (a * b) * c = a * (b * c)  [(a * b)]
	#Reemplazando en asociativa

	aso = "(a * b)" # * c
	aso1 = "(a * c)"
	aso3 = "a * b"
	asoR = aso.replace("a * b", e) #Sustituyendo a * b por la expresión ingresada
	asoR2 = aso1.replace("a * c", e) #Sustituyendo a * c por la expresión ingresada
	asoR3 = asoR2.replace("b", "c")  #Sustituyendo b de la expresión ingresada por c
	asoR4 = asoR3.replace("a","b") #Sustituyendo a de la expresión ingresada por b
	
	#Aplicando segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	mostrar.insert(tk.END, "\nProcedimiento: \n")
	mostrar.insert(tk.END, "\nTenemos que: [",e," = a * b ]\n")
	mostrar.insert(tk.END, "\nAplicamos la propiedad asociativa: \n")
	mostrar.insert(tk.END, "\nEn la propiedad asociativa: (a * b) * c = a * (a * c) \n")
	mostrar.insert(tk.END, "\nSe demuestra:\n")
	mostrar.insert(tk.END, asoR, " * c = a * ", asoR4)#primer paso: (2*a - b)  * c = a *  (2*b - c)
	mostrar.insert(tk.END, "\nPrimera igualdad: \n")
	mostrar.insert(tk.END, " a = ", asoR)
	mostrar.insert(tk.END, " \nb = c\n")
	mostrar.insert(tk.END, "\nSegunda igualdad: \n")
	mostrar.insert(tk.END, " a = a")
	mostrar.insert(tk.END, " b = ", asoR4)
	mostrar.insert(tk.END, "\nCon esto podemos entender que: a * b\n")

	if (resultado == resultado2):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\nQueda claro que la sigiente expresión:  (",e,")\n")
		mostrar.insert(tk.END,"\nSI CUMPLE, se trata de un monoide asociativo\n")
		return 1
	else:
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"Ha sido demostrado que la \nsiquiente expresión: (",e,")")
		mostrar.insert(tk.END,"NO CUMPLE, NO ES monoide \nasociativo ")

def monoideD(e):
	#aplicamos remplazo en asociativa
	aso = "(a + b)"
	aso1 = "(a + c)"
	aso3 = "a + b"
	asoR = aso.replace("a + b", e)
	asoR2 = aso1.replace("a + c", e)
	asoR3 = asoR2.replace("b", "c")
	asoR4 = asoR3.replace("a","b")
	
	#aplicamos segundo reemplazo.
	result = e.replace("b", "c")
	result2 = result.replace("a", asoR ) #2*(2*a - b) - c
	resultado = eval(result2)

	res = asoR.replace("b", "c")
	res1 = res.replace("a", "b")
	res2 = e.replace("b", res1)#2*a - (2*b - c)
	resultado2 = eval(res2)

	#2*(2*a - b) - c  =  2*a - (2*b - c)

	mostrar.insert(tk.END,"\nMuestra del procedimiento: \n")
	mostrar.insert(tk.END,"\nTenemos: [",e," = a + b ]")
	mostrar.insert(tk.END,"\nAplicamos la propiedad asociativa. . . \n")
	mostrar.insert(tk.END,"\n(a + b) + c = a + (a + c) \n")
	mostrar.insert(tk.END,"\nSe demuestra la propiedad: \n")
	mostrar.insert(tk.END,asoR, " + c = a + ", asoR4)#primer paso: (2*a - b)  + c = a +  (2*b - c)
	mostrar.insert(tk.END,"\nPrimera igualdad: \n")
	mostrar.insert(tk.END," a = ", asoR)
	mostrar.insert(tk.END," b = c")
	mostrar.insert(tk.END,"\nSegunda igualdad: \n")
	mostrar.insert(tk.END," \na = a\n")
	mostrar.insert(tk.END," \nb = ", asoR4)
	mostrar.insert(tk.END,"\nEs posible dar a entender que: a * b\n")

	if (resultado == resultado2):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\nSe demuestra que la siguiente expresión (",e,")\n")
		mostrar.insert(tk.END,"\nSI CUMPLE, ES UN monoide asociativo \n")
		return 1

		#Retornando 1 para la comprobación de grupo abeliano

	else:
		mostrar.insert(tk.END,"≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		mostrar.insert(tk.END,result2, " = ", res2)
		mostrar.insert(tk.END,"≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		mostrar.insert(tk.END,"Se demuestra que la siguiente ecueacion (",e,")")
		mostrar.insert(tk.END,"NO CUMPLE, NO SE TRATA DE UN monoide asociativo ")

def neutro(e): # elemento neutro
	for i in e:
		if (i == "/") :
			mostrar.insert(tk.END,"La división no es un operador alojado por el Elemento Neutro.")
			return 0
		elif ( i == "-") or (i == "+"):
			res2 = eval(e)
			neutro = 0
			neutro2 = 'e'
			mostrar.insert(tk.END,"\nProcedimiento :")
			mostrar.insert(tk.END,"\nSe aplica Elemento Neutro. . . \n")
			mostrar.insert(tk.END,"\nProcedimiento canónico. . .\n")
			mostrar.insert(tk.END,"\na + b => a + ae = a\n")
			mostrar.insert(tk.END,"\nae = a - a\n")
			mostrar.insert(tk.END,"\nae = 0\n")
			mostrar.insert(tk.END,"\ne = 0/a\n")
			mostrar.insert(tk.END,"\nPropiedad:\n")
			mostrar.insert(tk.END,"\n(",e,") + " ,neutro2," = ")
			mostrar.insert(tk.END,"\nEntones, la igualdad es. . . \n")
			mostrar.insert(tk.END,"\nEl valor de la expresión ingresada es: \n",res2)
			res = res2 + neutro
			if (res == res2):
				mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				mostrar.insert(tk.END,e, "+", neutro2)
				mostrar.insert(tk.END,"≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				mostrar.insert(tk.END,"\nExpresión (",e,") posee Elemento Neutro en la Adición (a + b)\n")
				return 1
			else:
				mostrar.insert(tk.END,"\nExpresión (",e,") no posee Elemento Neutro en la Adición (a + b)\n")
				return 0
		elif (i == "*"):
			res2 = eval(e)
			neutro = 1
			neutro2 = 'e'
			mostrar.insert(tk.END,"\nAplicando Elemento Neutro. . .\n")
			mostrar.insert(tk.END,"(",e,") * ",neutro2,"\n")
			res = res2 * neutro
			mostrar.insert(tk.END,"\nEntonces, la igualdad es: ")
			if (res == res2):
				mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				mostrar.insert(tk.END,e, "*", neutro2)
				mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
				mostrar.insert(tk.END,"\nLa expresión (",e,") SI posee Elemento Neutro \nen la MULTIPLICACIÓN (a * b)")
				return 1
			else:
				mostrar.insert(tk.END,"\nLa expresión (",e,") NO posee Elemento Neutro \nen MULTIPLICACIÓN (a * b)")
				return 0

# Elemento inverso
def inverso(e):
	#Aditivo inverso
	#Debe dar el elemento neutro
	Inver = "(-(a + b))"
	Inver = Inver.replace("a + b", e)
	res = eval(Inver)
	res2 = eval(e)
	#Aditivo multiplicativo
	Inver2 = "(1/(a + b))"
	Inver2 = Inver2.replace("a + b", e)
	res3 = eval(Inver2)
	res4 = eval(e)
	resT = (res4 * res3)

	mostrar.insert(tk.END,"\nPROCESO ADITIVO: ")
	mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
	mostrar.insert(tk.END,"\nPROCESO MULTIPLICATIVO: ")
	mostrar.insert(tk.END,"\nAplicando Elemento Inverso. . . ")
	mostrar.insert(tk.END,"\nTenemos que, la igualdad es: ")
	if ((res2 + res) == 0) and (resT == 1):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
		mostrar.insert(tk.END,e, "+", Inver, "ADITIVO")
		mostrar.insert(tk.END,e, "+", Inver2, "MULTIPLICATIVO")
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\nLa expresión (",e,") SI tiene Elemento Inverso ADITIVO [",Inver,"]\n")
		mostrar.insert(tk.END,"\nLa expresión (",e,") SI tiene Elemento Inverso MULTIPLICATIVO [",Inver2,"]\n")
		return 1
		# retornando 1 para la comprobacion de grupo abeliano
	else:
		mostrar.insert(tk.END,"\nLa expresión (",e,") NO tiene Elemento Inverso ADITIVO ó MULTIPLICATIVO \n[",Inver,"] o [",Inver2,"]")
		return 0

 # Verificando si es grupo
def conmutatividad(e): #Grupo
	conmu = e.replace("b","l")
	conmu = conmu.replace("a","b")
	conmu = conmu.replace("l","a")

	mostrar.insert(tk.END,"\nProcedimiento: \n")
	mostrar.insert(tk.END,"\nTenemos: (",e," = b + a )\n")
	mostrar.insert(tk.END,"\nAplicamos la propiedad conmutativa: \n")
	mostrar.insert(tk.END,"\nTenemos: a + b = a + b\n")
	mostrar.insert(tk.END,"\nSe demuestra: \n")

	if (eval(e) == eval(conmu)):
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"La siquiente expresión (",e,")\n")
		mostrar.insert(tk.END,"\nSI CUMPLE con la Propiedad Conmutativa.\n")
		mostrar.insert(tk.END,"\nSI es un Grupo Abeliano.\n")
	else:
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n")
		mostrar.insert(tk.END,"\nSe de muestra que la siquiente ecueacion (",e,")")
		mostrar.insert(tk.END,"\nNO CUMPLE con la Propiedad Conmutativa.")
		mostrar.insert(tk.END,"\nNO es un Grupo Abeliano.")
# Obteniendo valor de la segunda expresión 
def segunda_expr():

	while True:

		try:
			#Linkear este input a la segunda inputbox ####################################
			expr2 = textArea2.get()
			resultado2 = eval(expr2)
			return expr2

		except ValueError:
			mostrar.insert(tk.END,"La segunda expresión no es válida. Ingrese nuevamente.")

# Función para la elaboración de la propiedad distributiva
def propiedadDistributiva(e1, e2):
	#a*(b+c)
	elm = e1.replace("b","c")
	elm = elm.replace("a","b")
	dist1 = e2.replace("b","("+elm+")")
	r1 = eval(dist1)

	#a*b+a*c
	dist2 = "(a * b) + (a*c)"
	elm1 = e2.replace("b","c")
	dist2 = dist2.replace("a*b",e2)
	dist2 = dist2.replace("a*c",elm1)
	r2 = eval(dist2)
	mostrar.insert(tk.END,"\nPropiedad Distributiva")
	mostrar.insert(tk.END,dist1, "debe ser igual a ",dist2)

	if (r1 == r2):
		mostrar.insert(tk.END,"\nLa expresión es anillo.")
		return 1
		# retornando 1 para la comprobacion de cuerpo
	else:
		mostrar.insert(tk.END,"La expresión no es anillo.")

# Comprobación de números reales.
def reales(e):
	#Obteniendo valor numérico de la expresión ingresada
	numerico = eval(e)

	#Comprobando si es real
	if (isinstance(numerico, complex)):
		mostrar.insert(tk.END,"No cumple la Ley de Composición Interna. NO es un número real.")
		return 0
	else:
		mostrar.insert(tk.END,"Cumple con la Ley de Composición Interna. Es un número real.")
		return 1

## MODIFICAR LOS PRINT EN ARRANCA POR MOSTRAR.INSERT

def arranca():
    
    opcion = int(v.get())

    #Entero
    if opcion == 1:

        while True:

            try:
                expresion = str(textArea1.get())
                resultado = eval(expresion)

                if (isinstance(resultado,int)):
                    mostrar.insert(tk.END, "La expresión ingresada cumple la Ley de Composición Interna.")
                    
                    monoideA(expresion)
                    monoideB(expresion)

                    
                    if (neutro(expresion) == 1):
                        if (inverso(expresion) == 1):
                            conmutatividad(expresion)
                            label5.config(state=NORMAL)
                            textArea2.config(state=NORMAL)
                            messagebox.showinfo(message="Ya puede introducir la segunda ecuacion!\nProceda a hacerlo y presionar 'Comprobar 2'", title="Aviso")
                            boton2.config(state=NORMAL)
							# expr2 = segunda_expr()
                            # print("La segunda expresión es: ",expr2)
                            # resultado2 = eval(expr2)
                            # if (isinstance(resultado2, int)):
                            #     print("La segunda expresión cumple con la Ley de Composición Interna")
                            #     print("Comprobando MONOIDE ASOCIATIVO. . .")

                            #     if (monoideC(expr2) == 1):
                            #         m+=1
                            #     if (monoideD(expr2) == 1):
                            #         m+=1	
                            #     if (propiedadDistributiva(expresion, expr2) == 1):
                            #         m+=1
                            #     if (m == 2):
                            #         print("\nLa segunda expresión ingresada es SEMIGRUPO.")
                            #     if (m ==3 ):
                            #         print("\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
                            #     else:
                            #         print("\nNO hay CUERPO. No se cumple tanto Grupo Abeliano como Propiedad Distributiva")
                            #     print("Fin del programa.")
                            break #Fin del ciclo

                        else:
                            mostrar.insert(tk.END,"\nNo se cumple el Elemento Inverso. No pertenece. Fin del programa.")
                            messagebox.showinfo(message="\nNo se habilitara la entrada de la segunda operacion.\n Esto debido a que no hay elemento inverso", title="Aviso")
                            break
                    else:
                        mostrar.insert(tk.END,"\nNo se cumple el Elemento Neutro. No pertenece. Fin del programa")
                        break
                        
                else:
                    mostrar.insert(tk.END,"\nLa expresión ingresada (",expresion,") NO cumple la Ley de Composición Interna. \nSu resultado es: ",resultado," ")
                    break
            except NameError:
                mostrar.insert(tk.END,"\nExpresión ingresada no es válida. \nPor favor, intente nuevamente.")
                break
				

    #Natural
    elif opcion == 2:

        while True:
            mostrar.insert(tk.END,"\nHa escogido trabajar con el conjunto de los números naturales. \n")

            try:
                expresion = str(textArea1.get())
                resultado = eval(expresion)

                if (resultado >= 0 and isinstance(resultado,int)):
                    mostrar.insert(tk.END,"La expresión (",expresion,") cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)
                    monoideA(expresion)
                    monoideB(expresion)

                    if (neutro(expresion) == 1):
                        if (inverso(expresion) == 1):
                            mostrar.insert(tk.END,"\nPertenece a grupo.")
                            conmutatividad(expresion)
                            label5.config(state=NORMAL)
                            textArea2.config(state=NORMAL)
                            messagebox.showinfo(message="Ya puede introducir la segunda ecuacion!\nProceda a hacerlo y presionar 'Comprobar 2'", title="Aviso")
                            boton2.config(state=NORMAL)
                            break

                           # expr2 = segunda_expr()
                           # print("La segunda expresión es: ",expr2)
                           # resultado2 = eval(expr2)
                           # if (resultado2 >= 0 and isinstance(resultado2, int)):
                           #     mostrar.insert(tk.END,"La segunda expresión cumple con la Ley de Composición Interna")
                           #     if (monoideC(expr2) == 1):
                           #         m+=1
                           #     if (monoideD(expr2) == 1):
                           #         m+=1	
                           #     if (propiedadDistributiva(expresion, expr2) == 1):
                           #         m+=1
                           #     if (m == 2):
                           #         mostrar.insert(tk.END,"\nLa segunda expresión ingresada es SEMIGRUPO.")
                           #     if (m == 3):
                           #         mostrar.insert(tk.END,"Hay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva")
                           #     else:
                           #         mostrar.insert(tk.END,"NO hay Cuerpo. No se cumple Grupo Abeliano en conjunto con Propiedad Distributiva")
                           #     mostrar.insert("Fin del programa.")
                                #break

                            #else:
                              #  mostrar.insert(tk.END,"La segunda expresión NO cumple con la Ley de Composición Interna")
                        else:
                            mostrar.insert(tk.END,"No se cumple Elemento Inverso. No pertenece. Fin del programa.")
                            break
                    else:
                        mostrar.insert(tk.END,"No se cumple Elemento Neutro. No pertenece. Fin del programa.")
                        break
                else:
                    mostrar.insert(tk.END,"La expresión (",expresion,") no cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)
                    mostrar.insert(tk.END,"Fin del programa.")
                    break
            except NameError:
            	mostrar.insert(tk.END,"Expresión ingresada no es válida, intente nuevamente.")
            	print("Expresión ingresada no es válida, intente nuevamente.")
            	break

    #Real
    elif opcion == 3:

        while True:
            mostrar.insert(tk.END,"\nHa escogido trabajar con el conjunto de los números reales. Por favor, ingrese la expresión matemática a comprobar: ")

            try:
                expresion = str(textArea1.get())
                resultado = eval(expresion)
                if (isinstance(resultado,complex)):
                    mostrar.insert(tk.END,"La expresión ingresada (",expresion,") NO cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)
                    break
                else:
                    mostrar.insert(tk.END,"La expresión ingresada (",expresion,") cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)
                    monoideA(expresion)
                    monoideB(expresion)
                    if (neutro(expresion) == 1):
                        if (inverso(expresion) == 1):
                            conmutatividad(expresion)
                            label5.config(state=NORMAL)
                            textArea2.config(state=NORMAL)
                            messagebox.showinfo(message="Ya puede introducir la segunda ecuacion!\nProceda a hacerlo y presionar 'Comprobar 2'", title="Aviso")
                            boton2.config(state=NORMAL)
                            break

                            #expr2 = segunda_expr()
                            #mostrar.insert(tk.END,"La segunda expresión es: ",expr2)
                            #resultado2 = eval(expr2)
                            #mostrar.insert(tk.END,"Resultado numérico de la segunda expresión: ",resultado2)
                            #mostrar.insert(tk.END,"Comprobando si cumple Ley de Composición Interna. . .")
                            #if (reales(expr2) == 1):
                            #    if (monoideC(expr2) == 1):
                            #        m+=1
                            #    if (monoideD(expr2)	== 1):
                            #        m+=1
                            #    if (propiedadDistributiva(expresion, expr2) ==1):
                            #        m+=1
                            #    if (m == 2):
                            #        mostrar.insert(tk.END,"\nLa segunda expresión ingresada es SEMIGRUPO.")
                            #    if (m == 3):
                            #        mostrar.insert(tk.END,"\nHay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva")
                            #    else:
                            #        mostrar.insert(tk.END,"\nNO hay Cuerpo. NO se cumple tanto grupo Abeliano como Propiedad Distributiva")
                            #    mostrar.insert(tk.END,"\nFin del programa.")
                            #    break	
                            #else:
                             #   break
                        else:
                            mostrar.insert(tk.END,"No se cumple Elemento Inverso. No pertenece. Fin del programa.")
                            break
                    else:
                        mostrar.insert(tk.END,"No se cumple Elemento Neutro. No pertenece. Fin del programa")
                        break
            except NameError:
                mostrar.insert(tk.END,"Expresión ingresada no es válida, intente nuevamente.")

    #Complejos
    elif opcion == 4:

        while True:
            mostrar.insert(tk.END,"\nHa escogido trabajar con el conunto de los números complejos. Por favor, ingrese la expresión matemática a comprobar")

            try:
                expresion = str(textArea1.get())
                resultado = eval(expresion)
                if (isinstance(resultado, complex)):
                    mostrar.insert(tk.END,"La expresión ingresada (",expresion,") cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)

                    monoideA(expresion)
                    monoideB(expresion)

                    if (neutro(expresion) == 1):
                        if (inverso(expresion) == 1):
                            conmutatividad(expresion)
                            label5.config(state=NORMAL)
                            textArea2.config(state=NORMAL)
                            messagebox.showinfo(message="Ya puede introducir la segunda ecuacion!\nProceda a hacerlo y presionar 'Comprobar 2'", title="Aviso")
                            boton2.config(state=NORMAL)
                            break
                            #expr2 = segunda_expr()
                            #print("La segunda expresión es: ",expr2)
                            #resultado2 = eval(expr2)
                            #if (isinstance(resultado2, complex)):
                            #    print("La segunda expresión cumple con la Ley de Composición Interna")
                            #    if (monoideC(expr2) == 1):
                            #        m+=1
                            #    if (monoideD(expr2) == 1):
                            #        m+=1	
                            #    if (propiedadDistributiva(expresion, expr2) == 1):
                            #        m+=1
                            #    if (m == 2):
                            #        print("\nLa segunda expresión ingresada es SEMIGRUPO.")
                            #    if (m == 3):
                            #        print("\nHay CUERPO. Se cumple tanto Grupo Abeliano como Propiedad Distributiva.")
                            #    else:
                            #        print("\nNO hay Cuerpo. NO se cumple el Grupo Abeliano con la Propiedad Distributiva")
                            #    print("\nFin del programa.")
                            #    break
                        else:
                            mostrar.insert(tk.END,"\nNo se cumple Elemento Inverso. No pertenece. Fin del programa.")
                            break
                    else:
                        mostrar.insert(tk.END,"\nNo se cumple Elemento Neutro. No pertenece. Fin del programa.")
                        break
                else:
                    mostrar.insert(tk.END,"La expresión ingresada (",expresion,") NO cumple con la Ley de Composición Interna.")
                    mostrar.insert(tk.END,"Resultado: ",resultado)
                    mostrar.insert(tk.END,"Fin del programa.")
                    break
            except NameError:
                mostrar.insert(tk.END,"Expresión ingresada no es válida, intente nuevamente.")

def bloquearVentanas():
	textArea1.config(state=DISABLED)
	textArea2.config(state=DISABLED)
	mostrar.config(state=DISABLED)
	boton1.config(state=DISABLED)
	boton2.config(state=DISABLED)
	radio1.config(state=DISABLED)
	radio2.config(state=DISABLED)
	radio3.config(state=DISABLED)
	radio4.config(state=DISABLED)
	messagebox.showinfo(message="Fin del programa.\n Si desea reutilizarlo debe reiniciar la aplicacion", title="Aviso")

def reset():
	print(" ")


def arranca2():

	#Trabajando con Enteros
	opcion = int(v.get())
	if opcion == 1:
		while True:

			try:
				expresion = str(textArea1.get())
				expr2 = segunda_expr()
				mostrar.insert(tk.END, "La segunda expresión es: ",expr2)
				resultado2 = eval(expr2)
				if (isinstance(resultado2, int)):
					mostrar.insert(tk.END, "La segunda expresión cumple con la Ley de Composición Interna")
					mostrar.insert(tk.END, "Comprobando MONOIDE ASOCIATIVO. . .")
					m = 0
					if (monoideC(expr2) == 1):
						m+=1
					if (monoideD(expr2) == 1):
						m+=1	
					if (propiedadDistributiva(expresion, expr2) == 1):
						m+=1
					if (m == 2):
						mostrar.insert(tk.END, "\nLa segunda expresión ingresada es SEMIGRUPO.")
					if    (m ==3 ):
						mostrar.insert(tk.END, "\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
					else:
						mostrar.insert(tk.END, "\nNO hay CUERPO. No se cumple tanto Grupo Abeliano como Propiedad Distributiva")
					mostrar.insert(tk.END, "Fin del programa.")
					bloquearVentanas()
					break
				else:
					mostrar.insert(tk.END,"La expresión ingresada no cumple con la Ley de Composición Interna")
					bloquearVentanas()
					break
			except NameError:
				mostrar.insert(tk.END,"Valor ingresado no es válido. Por favor inténtelo nuevamente.")
				print("Valor ingresado no es válido. Por favor, intente de nuevo.")
				break

	#Números naturales
	if opcion == 2:
		while True:
			try:
				expresion = str(textArea1.get())
				expr2 = segunda_expr()
				mostrar.insert(tk.END, "La segunda expresión es: ",expr2)
				resultado2 = eval(expr2)
				if (isinstance(resultado2, int) and (resultado2 >= 0)):
					mostrar.insert(tk.END, "La segunda expresión cumple con la Ley de Composición Interna")
					mostrar.insert(tk.END, "Comprobando MONOIDE ASOCIATIVO. . .")
					m = 0
					if (monoideC(expr2) == 1):
						m+=1
					if (monoideD(expr2) == 1):
						m+=1	
					if (propiedadDistributiva(expresion, expr2) == 1):
						m+=1
					if (m == 2):
						mostrar.insert(tk.END, "\nLa segunda expresión ingresada es SEMIGRUPO.")
					if    (m ==3 ):
						mostrar.insert(tk.END, "\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
					else:
						mostrar.insert(tk.END, "\nNO hay CUERPO. No se cumple tanto Grupo Abeliano como Propiedad Distributiva")
					mostrar.insert(tk.END, "Fin del programa.")
					bloquearVentanas()
					break
				else:
					mostrar.insert(tk.END,"La expresión ingresada no cumple con la Ley de Composición Interna")
					bloquearVentanas()
					break
			except NameError:
				mostrar.insert(tk.END,"Valor ingresado no es válido. Por favor, inténtelo nuevamente.")
				print("Valor ingresado no es válido. Por favor inténtelo nuevamente.")
				break

	#Tomando números reales
	if opcion == 3:
		while True:
			try:
				expresion = str(textArea1.get())
				expr2 = segunda_expr()
				mostrar.insert(tk.END, "La segunda expresión es: ",expr2)
				resultado2 = eval(expr2)
				if (isinstance(resultado2, complex)):
					mostrar.insert(tk.END,"La expresión ingresada no cumple con la Ley de Composición Interna")
					bloquearVentanas()
					break
				else:
					mostrar.insert(tk.END, "La segunda expresión cumple con la Ley de Composición Interna")
					mostrar.insert(tk.END, "Comprobando MONOIDE ASOCIATIVO. . .")
					m = 0
					if (monoideC(expr2) == 1):
						m+=1
					if (monoideD(expr2) == 1):
						m+=1	
					if (propiedadDistributiva(expresion, expr2) == 1):
						m+=1
					if (m == 2):
						mostrar.insert(tk.END, "\nLa segunda expresión ingresada es SEMIGRUPO.")
					if    (m ==3 ):
						mostrar.insert(tk.END, "\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
					else:
						mostrar.insert(tk.END, "\nNO hay CUERPO. No se cumple tanto Grupo Abeliano como Propiedad Distributiva")
					mostrar.insert(tk.END, "Fin del programa.")
					bloquearVentanas()
					break
			except NameError:
				mostrar.insert(tk.END,"Valor ingresado no es válido. Por favor, inténtelo nuevamente.")
				print("Valor ingresado no es válido. Por favor inténtelo nuevamente.")
				break

	#Tomando números complejos
	if opcion == 4:
		while True:

			try:
				expresion = str(textArea1.get())
				expr2 = segunda_expr()
				mostrar.insert(tk.END, "La segunda expresión es: ",expr2)
				resultado2 = eval(expr2)
				if (isinstance(resultado2, complex)):
					mostrar.insert(tk.END, "La segunda expresión cumple con la Ley de Composición Interna")
					mostrar.insert(tk.END, "Comprobando MONOIDE ASOCIATIVO. . .")
					m = 0
					if (monoideC(expr2) == 1):
						m+=1
					if (monoideD(expr2) == 1):
						m+=1	
					if (propiedadDistributiva(expresion, expr2) == 1):
						m+=1
					if (m == 2):
						mostrar.insert(tk.END, "\nLa segunda expresión ingresada es SEMIGRUPO.")
					if    (m ==3 ):
						mostrar.insert(tk.END, "\nHay CUERPO. Se cumple tanto GRUPO ABELIANO como PROPIEDAD DISTRIBUTIVA")
					else:
						mostrar.insert(tk.END, "\nNO hay CUERPO. No se cumple tanto Grupo Abeliano como Propiedad Distributiva")
					mostrar.insert(tk.END, "Fin del programa.")
					bloquearVentanas()
					break
				else:
					mostrar.insert(tk.END,"La expresión ingresada no cumple con la Ley de Composición Interna")
					bloquearVentanas()
					break
			except NameError:
				mostrar.insert(tk.END,"Valor ingresado no es válido. Por favor inténtelo nuevamente.")
				print("Valor ingresado no es válido. Por favor, intente de nuevo.")
				break

'''</CODIGO>'''


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
v = tk.StringVar()
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
instrucciones.insert(tk.END, '1)Seleccione el conjunto numerico\n\n2)Introduzca las ecuaciones\n\n3)Presione el boton de comprobar\n\n4)Las comprobaciones seran mostradas\n en el cuadro inferior')
instrucciones.config(state=DISABLED)
#label integrantes
integrantes = tk.Label(ROOT, text="Sebastian Avendaño, V-26.765.567.\nSebastian Alvarez V-26.900.740")
integrantes.place(x=550, y=550)
#label ecuacion 1
label4 = tk.Label(ROOT, text="Ecuacion 1")
label4.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
label4.place(x=63, y=215)
#label ecuacion 2
label5 = tk.Label(ROOT, text="Ecuacion 2")
label5.config(font=("Menlo", 9), bg="#17212C", fg="#FFFFFF")
label5.place(x=300, y=215)
label5.config(state=DISABLED)
#text area ecuacion 1
textArea1 = tk.Entry(ROOT)
textArea1.place(x=40, y=240)
textArea1.insert(0, "")
#text area ecuacion 2
textArea2 = tk.Entry(ROOT)
textArea2.place(x=275, y=240)
textArea2.insert(0, "")
textArea2.config(state=DISABLED)
#widget boton 1
boton1 = tk.Button(ROOT, text="Comprobar 1", command=arranca)
boton1.config(font=("bold"))
boton1.place(x=50, y=280)
#widget boton 2
boton2 = tk.Button(ROOT, text="Comprobar 2", command=arranca2)
boton2.config(font=("bold"))
boton2.place(x=285, y=280)
boton2.config(state=DISABLED)
#widget boton reset
reset = tk.Button(ROOT, text="Reset", command=reset)
reset.place(x=203, y=280)
#radio buttons
radio1 = tk.Radiobutton(ROOT, text="ENTEROS", variable = v, value=1)
radio1.place(x=20, y=160)
radio2 = tk.Radiobutton(ROOT, text="NATURALES", variable = v, value=2)
radio2.place(x=120, y=160)
radio3 = tk.Radiobutton(ROOT, text="REALES", variable = v, value=3)
radio3.place(x=230, y=160)
radio4 = tk.Radiobutton(ROOT, text="COMPLEJOS", variable = v, value=4)
radio4.place(x=320, y=160)
radio3.select()
#separator
separador1 = Separator(ROOT, orient=VERTICAL).place(x=480, y=80, height=500)
separador2 = Separator(ROOT, orient=HORIZONTAL).place(x=45, y=340, width=390)
#scrollbar
scroll = Scrollbar(ROOT)
scroll.place(x = 428, y = 385, height=200)
#Text widget para resultado de comprobaciones
mostrar = tk.Text(ROOT, height=17, width=50)
mostrar.config(font=("Menlo", 9), fg="#FFFFFF", bg="#31475e", borderwidth=4, relief=SUNKEN)
mostrar.place(x=65, y=365)
#mostrar.config(state=DISABLED)
#configurar scroll
scroll.config(command=mostrar.yview)

'''</WIDGETS>'''

#Main loop
ROOT.mainloop()




        

    


