import tkinter as tk
from tkinter import messagebox

class RangoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Rango de 0-20")
        
        self.numero_label=tk.Label(root, text="Ingrese un numero")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(root)
        self.numero_entry.pack()
        
        self.Comprobar_button=tk.Button(root, text="Comprobar numero", command=self.Comprobar_num)
        self.Comprobar_button.pack()

    def Comprobar_num(self):
        try:
            numero=float(self.numero_entry.get())
            
            if numero>0 and numero<21:
                messagebox.showinfo("Número en el rango", f"El número que se encuentra del rango fue: {numero}")
                
            else:
                self.numero_entry.delete(0, tk.END)
                self.numero_entry.focus()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")


if __name__== "__main__":
    root=tk.Tk()
    RangoApp=RangoApp(root)
    root.mainloop()
    