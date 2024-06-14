import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luis
apellido: Duran
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        positivos = 0
        negativos = 0 
        cantidadPositivos = 0
        cantidadNegativos = 0
        cantidadCeros = 0
        diferencia = 0
        

        while True:
            verificador = prompt("Verificador", "Coloca aca los numeros")
            
            if verificador == "":
                alert("Error", "Debes colocar un numero")
                continue

            if verificador == None:
                break

            if verificador == "0":
                cantidadCeros += 1

            if int(verificador):
                
                if int(verificador) > 0:
                    positivos += int(verificador)
                    cantidadPositivos += 1

                if int(verificador) < 0:
                    negativos += int(verificador)
                    cantidadNegativos += 1

        diferencia = cantidadPositivos - cantidadNegativos

        if diferencia < 0:
            diferencia = diferencia * -1

        if cantidadCeros or positivos or negativos:
            alert("Verificador", f"Positivos: {cantidadPositivos}, Negativos: {cantidadNegativos}, Suma de positivos: {positivos}, Suma de negativos: {negativos}, Cantidad de Ceros: {cantidadCeros}, Diferencia: {diferencia}")

        else:
            alert("Error", "Debes colocar numeros")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
