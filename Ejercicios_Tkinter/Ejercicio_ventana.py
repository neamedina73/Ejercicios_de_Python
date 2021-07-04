import tkinter

ventana = tkinter.Tk()
ventana.geometry("1200x1200")
def saludo():
    print("Hola")
boton1 = tkinter.Button(ventana, text="Presiona aquí.", command= saludo)
boton1.pack()
ventana.mainloop()