import os
# VARIABLES DECLARADAS
arroz_con_pato, jarras_chicha = 0 , 0

# imput
arroz_con_pato = int(os.sys.argv [ 1 ])
jarras_chicha = int(os.sys.argv [ 2 ])

# procesando
total = ( arroz_con_pato + jarras_chicha )

# Verificador
total = (total <  50  or total >  100 )

# Validar el total de lo consumido
total_invalido = True
while (total_invalido):
    total = int(input( " ingrese total: " ))
    total_invalido = (total <  50  or total >  100 )
# fin_while
print ( " fin del bucle " )
