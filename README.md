# agregacion_composicion

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/GonzaloGmv/agregacion_composicion)

# Ejercicio a. El día siguiente

El UML de este ejercicio es el siguiente:

![ejra drawio](https://user-images.githubusercontent.com/91721237/160280172-462837cd-c275-4d39-a8dc-ef5beb99000a.png)

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

La manera que he encontrado para que la interrogación vaya al final es la siguiente:
```
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido")
        print("?")
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
print(yang is yin.yang)
del(yang)
```
El UML de este código sería el siguiente:

![ejrb drawio](https://user-images.githubusercontent.com/91721237/160280193-f6c32261-994b-437a-ad26-8943c5f5d254.png)


# Ejercicio c. Alternativa a la herencia múltiple

El UML de este ejercicio es el siguiente:

El código de este ejercicio es el siguiente:

# main

El código del main es el siguiente:
```
from clases.ejra import *
from clases.ejrb import *
from clases.ejrc import *

if __name__ == '__main__':
    while True:
        ejr = input("Escriba el numero del ejercicio que desea iniciar, a, b o c: ")
        try:
            ejr == 'a' or ejr == 'b' or  ejr == 'c'
        except:
            pass
        else:
            break
    if ejr == 'a':
        ciudad = input("¿Que ciudad quiere destruir, NY o LA? ")
        if ciudad == "NY" or ciudad == "ny":
            ny = NewYork()
            del ny
        elif ciudad == "LA" or ciudad == "la":
            la = LosAngeles()
            del la
        else:
            print("No es una ciudad válida")
    
    elif ejr == 'b':
        yin = Yin() 
        yang = Yang() 
        yin.yang = yang 
        print(yang) 
        print(yang is yin.yang)
        del(yang)
    
    elif ejr == 'c':
        pared_norte = pared("NORTE") 
        pared_oeste = pared("OESTE") 
        pared_sur = pared("SUR") 
        pared_este = pared("ESTE")
        ventana_norte = ventana(pared_norte, 0.5) 
        ventana_oeste = ventana(pared_oeste, 1) 
        ventana_sur = ventana(pared_sur, 2) 
        ventana_este = ventana(pared_este, 1)
        casa = casa([pared_norte, pared_oeste, pared_sur, pared_este], '', '') 

        print(casa.superficieacristalada())
```     
