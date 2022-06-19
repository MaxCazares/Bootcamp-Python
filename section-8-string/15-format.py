# 1 - Sin posición, index asignado

name = "Resident Evil 2 Remake"

# 1.1 - Con un valor

a = "Mi juego favorito es {}".format(name) 
# Mi juego favorito es Resident Evil 2 Remake

# 1.2 - Con más de un valor

name_first_game = "Resident Evil 2"
name_second_game = "Resident Evil 3"
a = "Mis juegos favoritos son: {} y {}".format(
    name_first_game, name_second_game)
# Mis juegos favoritos son Resident Evil 2 y Resident Evil 3

# 2 - Asignando posición index para especificar como ordenarlo

name_third_game = "CupHead"
a = "Mis juegos favoritos son: {1}, {2} y {0}".format(
    name_first_game, name_second_game, name_third_game)

print("Final")