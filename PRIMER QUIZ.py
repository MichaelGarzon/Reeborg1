''' Pimer quiz: Este es un programa diseñado para
que reeborg consiga una manzana, la reemplace por una
banana y vuleva a casa
Autor: Michael Garzon Pachon
Fecha: 29/07/19'''

# Llegar a la manzana
print("Hola soy reeborg")
print("Voy a hacer una mision")
repeat 4:
    move()
#pause()

# Reemplazar la manzana
take("apple")
put("banana")
#pause()

# Volver a home
repeat 2:
    turn_left()
    #pause()
repeat 4:
    move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
