class NewYork:
    def __del__(self): 
        print("Destrucción Nueva York") 

    def __init__(self):
        self.edificios = [edificio(name) for name in ["Edificio A", "Edificio B"]] 
        self.empleado = [empleado(name) for name in ["Sr. Martin", "Sr. Salim"]]

class LosAngeles:
    def resiste(self): 
        print("Destruccion Los Angeles") 

    def __init__(self):
        self.edificios = [edificio(name) for name in ["Edificio C"]] 
        self.empleado = [empleado(name) for name in ["Sra. Xing"]]
 
class edificio: 
    def __del__(self): 
        print("Destrucción {}".format(self.name)) 
 
    def __init__(self, name): 
        self.name = name 
    
class empleado:
    def __del__(self): 
        print("Muerte de {}".format(self.name)) 
 
    def __init__(self, name): 
        self.name = name 