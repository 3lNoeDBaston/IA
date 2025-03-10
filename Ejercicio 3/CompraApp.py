import tkinter as tk
from tkinter import messagebox
from Compra import Compra

class CompraApp:
     def __init__(self, root):
        self.root=root
        self.root.title("Calcular precio del producto")
          
        self.mes_label=tk.Label(root, text="Ingrese el mes de compra")
        self.mes_label.pack()
        self.mes_entry=tk.Entry(root)
        self.mes_entry.pack()
          
        self.precio_label=tk.Label(root, text="Ingrese el precio")
        self.precio_label.pack()
        self.precio_entry=tk.Entry(root)
        self.precio_entry.pack()
          
          
        self.Calcular_button=tk.Button(root, text="Calcular el total", command=self.Calcular_total)
        self.Calcular_button.pack()
          
     def Calcular_total(self):
         mes=self.mes_entry.get()
         precio=float(self.precio_entry.get())
         descuento=Compra(mes,precio)
         Total=descuento.Calcular_descuento()
         Tpagar=descuento.Nuevo_precio()
         messagebox.showinfo("El total a pagar es", f"Descuento:${Total:.2f}\nTotalPagar:${Tpagar:.2f}")
         
if __name__=="__main__":
    root=tk.Tk()
    CompraApp=CompraApp(root)
    root.mainloop()
        
         
        