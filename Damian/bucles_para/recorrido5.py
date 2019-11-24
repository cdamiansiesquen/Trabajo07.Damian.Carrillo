# hallar la suma de los "x" numeros desde el 20
import os
# input
x = int (os.sys.argv [ 1 ])
i = 20
suma = 0
while(i <= x):
    suma += i
    i +=  1
# fin_while

print ( " La suma de los dichos primeros numeros despues del 20 es: " , suma)
