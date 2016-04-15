'''
   realizar una suma de todos los numeros pares
   entre 10 y 5000 sin contemplar a 100 y 1000

'''


sum = 0
for cont in range(10,5001):
    if (cont % 2) == 0:
        if cont == 100 or cont == 1000:
            pass
        sum = sum + cont

#Termina el for

print(str(sum) + " este es el numero total")