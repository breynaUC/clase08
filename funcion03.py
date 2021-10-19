from tkinter import *
import math
win = Tk()
n = IntVar()
opcion = IntVar()
res = DoubleVar()
def raiz(n):
    return math.sqrt(n)
def potencia(n):
    return math.pow(n,5)
def logaritmo(n):
    return math.log10(n)
def calcular():
    x = n.get()
    if opcion.get()==1:
        res.set(raiz(x))
    elif opcion.get()==2:
        res.set(potencia(x))
    elif opcion.get()==3:
        res.set(logaritmo(x))
    else:
        res.set(0)


    
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
label_numero = Label(win, text="Número:")
label_numero.grid(row=1, column=1, sticky=E)
entry_numero = Entry(win, textvariable=n, width=30)
entry_numero.grid(row=1, column=2, sticky=E+W)
radio_raiz = Radiobutton(win, text="Raiz", variable=opcion, value=1)
radio_raiz.grid(row=2,column=2, sticky=W)
radio_potencia = Radiobutton(win, text="Potencia", variable=opcion, value=2)
radio_potencia.grid(row=3,column=2, sticky=W)
radio_loga = Radiobutton(win, text="Logaritmo", variable=opcion, value=3)
radio_loga.grid(row=4,column=2, sticky=W)
boton_calcular= Button(win, command=calcular, background="green",fg="white", text="Calcular")
boton_calcular.grid(row=5,column=2, sticky=W)
label_resultado = Label(win, text="Resultado:")
label_resultado.grid(row=6, column=1, sticky=E)
entry_resultado = Entry(win, textvariable=res, width=30)
entry_resultado.grid(row=6, column=2, sticky=E+W)
win.geometry('300x300')
win.mainloop()