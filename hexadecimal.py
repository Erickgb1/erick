import tkinter as tk 

def cambiar_fuente_saludo():
    print("hola")
    etiqueta_saludo.config(font=("Comic Sans MS", 20))

def cambiar_texto_saludo():
    etiqueta_saludo.config(text="adios")

def cambiar_fuente_saludo_alt(): 


    etiqueta_saludo.config(font=("Arial Black", 25))

def cambiar_color_saludo():
    etiqueta_saludo.config(fg="green")

def actualizar_etiqueta_entrada():
    etiqueta_numero.config(text=campo_entrada_secreto.get())


ventana_principal = tk.Tk()
ventana_principal.geometry("900x500")
ventana_principal.title("Miércoles de plaza 2x1")


etiqueta_saludo = tk.Label(ventana_principal, text="Hola", font=("Arial", 35))
etiqueta_saludo.pack(side="top")

etiqueta_numero = tk.Label(ventana_principal, text="123456789", font=("Arial", 40))
etiqueta_numero.place(x=300, y=380)


boton_cambiar_texto = tk.Button(ventana_principal, text="Cambiar Texto", command=cambiar_texto_saludo)
boton_cambiar_texto.place(x=700, y=100)

boton_cambiar_fuente = tk.Button(ventana_principal, text="Cambiar Fuente", command=cambiar_fuente_saludo_alt)
boton_cambiar_fuente.place(x=700, y=200)

boton_cambiar_color = tk.Button(ventana_principal, text="Cambiar Color", command=cambiar_color_saludo)
boton_cambiar_color.place(x=700, y=300)


campo_entrada_secreto = tk.Entry(ventana_principal, show="*")
campo_entrada_secreto.place(x=380, y=200)


boton_actualizar_entrada = tk.Button(ventana_principal, text="Actualizar Entrada", command=actualizar_etiqueta_entrada)
boton_actualizar_entrada.place(x=300, y=200) 


try:
    imagen_duki = tk.PhotoImage(file="E:\imagen)
    etiqueta_imagen = tk.Label(ventana_principal, image=imagen_duki)
    etiqueta_imagen.place(x=100, y=100)
except tk.TclError:
    print("Advertencia: No se pudo cargar 'Duki.png'. Asegúrate de que el archivo existe y la ruta es correcta.")
    
    etiqueta_sin_imagen = tk.Label(ventana_principal, text="[Imagen no encontrada]", font=("Arial", 12))
    etiqueta_sin_imagen.place(x=100, y=100)



ventana_principal.mainloop()

