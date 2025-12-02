import tkinter 
ventana = tkinter.Tk()
ventana.title("Examen de Python")
ventana.geometry("400x400")
ventana.boton = tkinter.Button(ventana, text="ordenar numeros")
ventana.boton.pack()

ventana.texbox = tkinter.Text(ventana, height=1, width=1)
ventana.texbox.pack()
ventana.texbox1 = tkinter.Text(ventana, height=1, width=1)
ventana.texbox1.pack()
ventana.texbox2 = tkinter.Text(ventana, height=1, width=1)
ventana.texbox2.pack()
ventana.texbox3 = tkinter.Text(ventana, height=1, width=1)
ventana.texbox3.pack()
ventana.texbox4 = tkinter.Text(ventana, height=1, width=1)
ventana.texbox4.pack()
ventana.texbox5 = tkinter.Text(ventana, height=1, width=1)
ventana.texbox5.pack()


print("introduce 5 numeros ")
num1=int(input("numero 1: "))
num2=int(input("numero 2: "))
num3=int(input("numero 3: "))
num4=int(input("numero 4: "))
num5=int(input("numero 5: "))
 
lista=[num1,num2,num3,num4,num5]
if num1<num2:
    remove=2
    num1=num2
if num2<num3:
    remove=num2
    num2=num3
if num3<num4:
    remove=num3
    num3=num4
if num4<num5:
    remove=num4
    num4=num5
  
print("los numeros ordenados son: ",num1,num2,num3,num4,num5) 













