# sumar los numeros que se encuentra entre "m" y "n"
import os
# input
m = int (os.sys.argv [ 1 ])
n = int (os.sys.argv [ 2 ])
a= m
suma = 0
while(a <= n):
    suma +=a
    a +=  2
# fin_while
print ( " la suma de los numeros que se diferencia en 2 unidades es: " , suma)
