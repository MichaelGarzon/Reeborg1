''' Actividad en clase: Este es un programa diseñado
para definir una funcion llamada walk, la cual es una 
caminata en un mundo de 5x5. Si no hay una pared
en frente, reeborg camina, en el caso de que no, no 
se hace nada.
Autor: Michael Grazón
Fecha: 29/07/19'''

def walk_zigzag():
    repeat 4:
        move()
        repeat 3:
            turn_left()
        move()
        turn_left()
walk_zigzag()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
