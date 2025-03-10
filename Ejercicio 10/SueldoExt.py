class Empleado:
    def __init__(self, nombre, horasN, horasExt, hijos):
        self.nombre= nombre
        self.horasN= horasN
        self.horasExt= horasExt
        self.hijos= hijos
    
    
    def Calcular_sueldoN(self):
        return self.horasN*100    


    def Calcular_horasExt(self):
        return self.horasExt*(150)
    
    
    def Calcular_hijos(self):
        return self.hijos*(100*0.05)
        
        
    def  Nuevo_salario(self):
        return self.Calcular_sueldoN()+ self.Calcular_horasExt()+ self.Calcular_hijos()
        
        