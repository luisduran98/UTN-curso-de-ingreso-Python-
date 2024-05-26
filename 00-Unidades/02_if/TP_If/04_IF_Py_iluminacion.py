import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Luis
apellido: Duran
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = float(self.combobox_cantidad.get())
        total = 0
        mensaje = 0

        if cantidad >= 6:
            precio = 800 * cantidad
            total =  precio - (precio * 0.5)
            mensaje = 50

        elif cantidad == 5 :
            precio = 800 * cantidad
            if marca == "ArgentinaLuz":
                total =  precio - (precio * 0.4)
                mensaje = 40
            else: 
                total =  precio - (precio * 0.3)
                mensaje = 30

        elif cantidad == 4:
            precio = 800 * cantidad
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                total =  precio - (precio * 0.25)
                mensaje = 25
            else:
                total =  precio - (precio * 0.20)
                mensaje = 20

        elif cantidad == 3:
            precio = 800 * cantidad
            if marca == "FelipeLamparas":
                total =  precio - (precio * 0.10)
                mensaje = 10
            elif marca == "ArgentinaLuz":
                total =  precio - (precio * 0.15)
                mensaje = 15
            else: 
                total =  precio - (precio * 0.05)
                mensaje = 5

        if total >= 4000:
            alert("Total", f"Genial conseguiste un descuento del {mensaje}% y sumaste otro mas de 5% y tu total es {total - (total * 0.05)}")
        
        else: alert("Total", f"Genial conseguiste un descuento del {mensaje}% y tu total es {total}")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()