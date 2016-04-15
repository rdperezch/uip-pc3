'''
github.com/ampotty/uip-pc3
Crear programa que maneje lista de supermercado donde se pueda agregar, ver, buscar y eliminar artículos. Los artículos
están en una tupla:
arroz
leche
tuna
cereal
jugo
'''

tup1 = ("arroz", "leche", "tuna", "cereal", "jugo")

opcion=0
x=0
y=0

suplist = []

while opcion != 4:
    print ("Si desea agregar productos a la lista presione 1")
    print ("Si desea ver los productos de la lista, presione 2")
    print ("Si desea eliminar productos de la lista presione 3")
    print ("Si desea salir, presione 4")
    opcion = input("Su Opción es: ")

    if opcion == "1": #Agregar
        print("desea agregar arroz ?, presione 1 ")
        print("desea agregar leche ?, presione 2  ")
        print("desea agregar tuna ?, presione 3  ")
        print("desea agregar cereal ?, presione 4  ")
        print("desea agregar jugo ?, presione 5 \n ")
        productos = input("Su Opción es: ")
        if productos == "1":
            suplist.append(tup1[0])
        elif productos == "2":
            suplist.append(tup1[1])
        elif productos == "3":
            suplist.append(tup1[2])
        elif productos == "4":
            suplist.append(tup1[3])
        elif productos == "5":
            suplist.append(tup1[4])
        else:
            print("no selecciono una opcion valida..")



    elif opcion == "2":
        print ("La lista de los productos para el super son: ", suplist)
        print("\n")


    elif opcion == "3":
        productos = 0
        while productos == 0:
            x = len(suplist)
            print("Para eliminar arroz, presione 1")
            print("Para eliminar leche, presione 2")
            print("Para eliminar tuna, presione 3")
            print("Para eliminar cereal, presione 4")
            print("Para eliminar jugo, presione 5")
            productos = int(input("Su opción es: "))
            while [y <= x]:
                if suplist[x] == tup1[productos]:
                    del suplist[x]
                    break
                else:
                    x = x+1

    else:
        print("no seleciono una opcion valida")