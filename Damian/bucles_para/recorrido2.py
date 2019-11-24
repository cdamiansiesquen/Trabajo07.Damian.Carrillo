# sumar los numeros que se encuentra entre "x" y "z"
import os
# input
x = int (os.sys.argv [ 1 ])
z = int (os.sys.argv [ 2 ])
i = x
suma = 0
while(i <= z):
    suma += i
    i +=  1
# fin_while
print ( " la suma de los numeros que estan entre dicho numeros  es: " , suma)
