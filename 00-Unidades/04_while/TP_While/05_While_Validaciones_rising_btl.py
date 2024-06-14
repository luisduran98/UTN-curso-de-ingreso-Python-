import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luis
apellido: Duran
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = ""
        edad = ""
        # estado = ""
        legajo = ""
        caso = 0
        
        while True:

            if caso == 0:
                validadorUno = prompt("Censo 2024", "Coloca tu apellido")

                if validadorUno == "":
                    alert("Error", "Debes colocar tu apellido")

                if validadorUno:
                    apellido = validadorUno
                    caso += 1

            if caso == 1:
                validadorDos = prompt("Censo 2024", "Coloca tu edad")

                if validadorDos == "":
                    alert("Atencion", "Debes colocar edad")
                    continue

                if int(validadorDos) >= 18 and int(validadorDos) <= 90:
                    edad = int(validadorDos)
                    caso += 1

                else:
                    alert("Atencion", "Debes ser mayor de 18 años para el censo")


            if caso == 2:

                indice = 0
                verificador = False

                validadorCuatro = prompt("Censo 2024", "Coloca tu legajo")

                if len(validadorCuatro) != 4:
                    alert("Atencion", "Verifica que el legajo tenga 4 numeros")
                    continue

                while indice < 4:
                    if validadorCuatro[indice] == "0":
                        verificador = True
                    
                    indice += 1

                if verificador == True:
                    alert("Atencion", "Verifica que el legajo no tenga ceros")


                else:
                    legajo = int(validadorCuatro)
                    break
            
        self.txt_apellido.delete(0,20)
        self.txt_edad.delete(0,20)
        self.txt_legajo.delete(0,20)

        self.txt_apellido.insert(0,apellido)
        self.txt_edad.insert(0,edad)
        self.txt_legajo.insert(0,legajo)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
