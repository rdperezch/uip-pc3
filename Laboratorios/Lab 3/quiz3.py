'''
    preguntara nombre de paciente
    si tiene dolor de cabeza
    si tiene alergia
    si tiene problema respiratorios
    dolor de cabeza
'''

cont= "n"

while cont == "n":
    nombre = input( " introduzca su nombre: ")

    h = input("tiene dolor de cabeza  ?  (S/N) ")
    s = input("tiene dolor de estomago   ?  (S/N) ")
    pr = input("tiene problemas respiratorios   ?  (S/N) ")


    if h == "s" and s == "s" and pr == "s":
        print(nombre + " se debe internar  ")

    elif h == "s" and s == "s":
        print(nombre + " Toma Paracetamol ")

    elif h == "s":
        print(nombre + " toma tylenol ")

    elif s == "s":
        print(nombre + " toma pepto Bismo ")

    elif pr == "s":
        print(nombre + " toma Norcetin")
    else:
        print(nombre + "se debe ir a la su casa")


    cont =input("desea continuar ? (S/N)")
    if cont == "s":
        break