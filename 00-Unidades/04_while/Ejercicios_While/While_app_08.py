import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luis
apellido: Duran
---
Ejercicio: while_08
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma = 0 
        multiplicacion = 1
        bandera = 0

        while True:
            numero = prompt("Suma y Promedio", "Coloca un numero")

            while numero == "":
                numero = prompt("Suma y Promedio", "Error, reingresar un numero")


            if numero == None or int(numero) == 0:
                break

            elif int(numero) > 0:
                suma = suma + int(numero)

            else:
                multiplicacion = multiplicacion * int(numero)
                bandera = 1
            
        self.txt_suma_acumulada.delete(0,20)
        self.txt_suma_acumulada.insert(0,suma)

        if bandera == 0:
            multiplicacion = 0

        self.txt_producto.delete(0,20)
        self.txt_producto.insert(0,multiplicacion)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
