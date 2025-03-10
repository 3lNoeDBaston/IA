import tkinter as tk
from  tkinter import messagebox
from SueldoExt import Empleado

class TotalApp:
    
    def __init__(self, root):
        self.root=root
        self.root.title("Calculo de salario total")
        
        self.nombre_label=tk.Label(root, text="Ingrese su nombre")
        self.nombre_label.pack()
        self.nombre_entry=tk.Entry(root)
        self.nombre_entry.pack()
        
        
        self.horasN_label=tk.Label(root, text="Ingrese las horas que trabajo")
        self.horasN_label.pack()
        self.horasN_entry=tk.Entry(root)
        self.horasN_entry.pack()
        
        self.horasExt_label=tk.Label(root, text="Ingrese las horas extras que trabajo")
        self.horasExt_label.pack()
        self.horasExt_entry=tk.Entry(root)
        self.horasExt_entry.pack()
        
        self.hijos_label=tk.Label(root,text="Ingrese los hijos que tiene")
        self.hijos_label.pack()
        self.hijos_entry=tk.Entry()
        self.hijos_entry.pack()
        
        
        self.CalculaT_button=tk.Button(root, text="Calcular salario total", command=self.Calcular_Total)
        self.CalculaT_button.pack()
        
    def Calcular_Total(self):
        nombre=self.nombre_entry.get()
        horas=int(self.horasN_entry.get())
        horasExt=int(self.horasExt_entry.get())
        hijitos=int(self.hijos_entry.get())
        
        usuario=Empleado(nombre,horas,horasExt,hijitos)
        Normales=usuario.Calcular_sueldoN()
        Extras=usuario.Calcular_horasExt()
        Thijos=usuario.Calcular_hijos()
        SueldoT=usuario.Nuevo_salario()
        
        
        
        messagebox.showinfo("Oda, sus datos son los siguientes",
                            f"Nombre:{nombre}\n"
                            f"Sueldo de horas normales: ${Normales}\n"
                            f"Sueldo de horas extras: ${Extras}\n"
                            f"Número de hijos: ${Thijos}\n"
                            f"Sueldo final: ${SueldoT}\n"
                            f"El sueldo por hora es de 100 y las horas extras es 50% más pagada que la normal"
                            )
        
        
        
        
        
        if __name__== "__main__":
            root=tk.Tk()
            TotalApp= TotalApp(root)
            root.mainloop()