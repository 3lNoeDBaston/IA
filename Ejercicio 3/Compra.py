class Compra:
    def __init__(self, mes, precio):
        self.mes=mes
        self.precio=precio
        
    def Calcular_descuento(self):
        if self.mes.lower()=="octubre":
            return self.precio * 0.15
        
        else:
            return self.precio *0
        
    
    def Nuevo_precio(self):
        return self.precio-self.Calcular_descuento()