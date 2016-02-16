"""
    Crear clase perro en quiz 4  5 úntos de vida 5 puntos de alegria
    caminar -2 de vida +1 de alegria
    correr -4 de vida +3 alegria
    dormir  +1 de vida -3 alegria
     jugar -3 de vida +4 de algria
     comer +5 de vida +1 de alegria

    Crear un objeto que se llame lassie
            lassie debe dormir, jugar,  comer , jugar , caminarm dirnur m cirrer m dirnur m dirnurm ciner


"""

class Perro:


    def __init__(self,puntos_vida=0,puntos_alegria=0):
        self.puntos_vida = puntos_vida
        self.puntos_alegria = puntos_alegria

    def caminar(self):
        self.puntos_vida -= 2
        self.puntos_alegria += 1


    def correr(self):
        self.puntos_vida -= 4
        self.puntos_alegria += 3

    def dormir(self):
        self.puntos_alegria -= 3
        self.puntos_vida += 1

    def jugar(self):
        self.puntos_vida -= 3
        self.puntos_alegria += 4

    def comer(self):
        self.puntos_vida += 5
        self.puntos_alegria += 1


x=5
y=5
conta = 0
lassie = Perro(x,y)

while conta != 10:

    lassie.dormir()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.jugar()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.comer()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.jugar()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.caminar()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.dormir()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.correr()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.dormir()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.dormir()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

    lassie.comer()
    if lassie.puntos_vida == 0:
        print("LASSIE MURIO :( ")
        break
    else:
        conta += 1

if conta == 10:
    print("Lassie sobrevio al juego")
    print("Puntos de Vida: "+ str(lassie.puntos_vida)+ "Puntos de alegria: "+ str(lassie.puntos_alegria))
else:
    print("Lassie no sobrevivio")
    print("Puntos de Vida: "+str(lassie.puntos_vida)+ "Puntos de alegria: "+ str(lassie.puntos_alegria))