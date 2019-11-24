import os
# VARIABLES DECLARADAS
masa, gravedad = 0 , 0

# imput
masa = int(os.sys.argv [ 1 ])
gravedad = int(os.sys.argv [ 2 ])

# procesando
peso = ( masa * gravedad)

# Verificador
peso = (peso <  500  or peso >  1500 )

# Validar el peso de cada lugar
peso_invalido = True
while (peso_invalido):
    peso = int(input( " ingrese peso: " ))
    peso_invalido = (peso <  500  or peso >  1500 )
# fin_while
print ( " fin del bucle " )
