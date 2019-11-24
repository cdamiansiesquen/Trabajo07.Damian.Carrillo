import os
# VARIABLES DECLARADAS
cemento, fierro = 0 , 0

# imput
cemento = int(os.sys.argv [ 1 ])
fierro = int(os.sys.argv [ 2 ])

# procesando
precio_total = ( cemento + fierro )

# Verificador
precio_total = (precio_total <  300  or precio_total >  500 )

# Validar el precio total de lo comprado
precio_total_invalido = True
while (precio_total_invalido):
    precio_total = int(input( " ingrese precio total: " ))
    precio_total_invalido = (precio_total <  300  or precio_total >  500 )
# fin_while
print ( " fin del bucle " )
