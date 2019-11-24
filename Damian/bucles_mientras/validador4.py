import os
# VARIABLES DECLARADAS
precio_llantas , carburador, embrague = 0 , 0, 0

# imput
precio_llantas = int(os.sys.argv [ 1 ])
carburador = int(os.sys.argv [ 2 ])
embrague = int(os.sys.argv [ 3 ] )

# processing
precio_total = ( precio_llantas + carburador + embrague )

# Verificador
precio_total = (precio_total <  200  or precio_total >  600 )

# Validar el precio total de lo comprado
precio_total_invalido = True
while (precio_total_invalido):
    precio_total = int(input( " ingrese precio total: " ))
    precio_total_invalido = (precio_total < 200  or precio_total >  600 )
# fin_while
print ( " fin del bucle " )
