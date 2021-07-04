import tkinter

ventana = tkinter.Tk()
ventana.geometry("1200x1200")
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg="green")
etiqueta.pack(fill=tkinter.X)
"""Se puede trabajar el atribito side, tkinter.BOTH, expand=true, fill=tkinter.Y"""
ventana.mainloop()