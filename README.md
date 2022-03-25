# agregacion_composicion

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/agregacion_composicion)

# Ejercicio a. El día siguiente

El código de este ejercicio es el siguiente:
```
class NewYork:
    def __del__(self): 
        print("Destrucción Nueva York") 

    def __init__(self):
        self.edificios = [edificio(name) for name in ["Edificio A", "Edificio B"]] 
        self.empleado = [empleado(name) for name in ["Sres. Martin", "Salim"]]
 
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
```

# Ejercicio b. ¿Inmortal?

El recolector de basura es una entidad que monitoriza las áreas de memoria y las libera cuando ya no se hace ninguna referencia a ellas, por esto mismo, la clase "Yang", sí que se elimina cuando se le ordena, pero la funcion __del__() no se ejecuta hasta el final.
Una manera de explicar esto, sería poner del(yang) una línea antes que print(yang). Esto daría error ya que la calse "Yang" ya ha sido destruida y no se puede imprimir, a continuación sí que se ejecutaría la funcion __del__() y se imprimiría el mensaje "Yang destruido", pero ya no se imprimiría la "?" debido al error.
