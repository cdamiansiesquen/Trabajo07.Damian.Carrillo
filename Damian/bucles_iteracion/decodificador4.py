# Decodificar msg encriptado
# P = mar frio
# Q = serrania esteparia
# R = paramo
# S = mar tropical
# T = bosque seco ecuatorial
# U = selva baja
import os
# input
msg = os.sys.argv [ 1 ].upper ()
# bucle
for letra in msg:
    if letra == "P":
        print("mar frio")
    if letra == "Q":
        print("serrania esteparia")
    if letra == "R":
        print("paramo")
    if letra == "S":
        print("mar tropical")
    if letra == "T":
        print("bosque seco ecuatorial")
    if letra == "U":
        print("selva baja")
# fin_iterador

print ( " Fin del bucle ")
