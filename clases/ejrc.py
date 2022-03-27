class pared: 
    def __init__(self, orientacion):
        self.orientacion=orientacion

class ventana(pared): 
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie=superficie

class casa(ventana):
    def __init__(self, paredes, orientacion, superficie):
        super().__init__(orientacion, superficie)
        self.paredes=paredes
    def superficieacristalada(self):
        return (self.paredes.superficie)