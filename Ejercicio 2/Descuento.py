class Usuario:
    def __init__(self, edad):
        self.edad= edad
        
        
    def calcular_descuento(self):
        if self.edad<10:
            return 50*0.25
            
        else:
            return 50*0.0
            
    def nuevo_precio(self):
        return 50-self.calcular_descuento()