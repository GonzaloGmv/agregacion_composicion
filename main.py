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