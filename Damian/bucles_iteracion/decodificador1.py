# Decodificar msg encriptado
# 1 = ¿que tal?
# 2 = espero estes mejor
# 3 = cuidate
# 4 = te quiero
import os
# input
msg = os.sys.argv [ 1 ].upper ()
# bucle
for letra in msg:
    if letra == "1":
        print("¿que tal?")
    if letra ==  "2":
        print("espero estes mejor")
    if letra ==  "3":
        print("cuidate")
    if letra ==  "4":
        print("te quiero")
# fin_iterador

print ( " Fin del bucle ")
