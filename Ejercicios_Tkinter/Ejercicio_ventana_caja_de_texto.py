import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x300")


boton1 = tkinter.Button(ventana, text = "click", command="textoDelaCaja")
boton1.pack()
ventana.mainloop()