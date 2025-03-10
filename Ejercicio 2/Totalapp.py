import tkinter as tk
from tkinter import messagebox
from Descuento import Usuario

class Totalapp:
    
    def __init__(self, root):
        self.root= root
        self.root.title("Calculo del precio a pagar por el juego")
        
        self.edad_label=tk.Label(root, text="Ingrese la edad")
        self.edad_label.pack()
        self.edad_entry=tk.Entry(root)
        self.edad_entry.pack()
        
         
        self.Calcular_button=tk.Button(root,text="calcular el boleto", command=self.Calcular_total)
        self.Calcular_button.pack()
        
    def Calcular_total(self):
        edad=int(self.edad_entry.get())
        descuento= Usuario(edad)
        total=descuento.calcular_descuento()
        TPagar=descuento.nuevo_precio()
        messagebox.showinfo("El total a pagar es", f"Total:${total:.2f}\nTotalPagar:${TPagar:.2f}")
            
            
            
        if __name__=="__main__":
              root=tk.Tk()
              Totalapp= Totalapp(root)
              root.mainloop()
            
            