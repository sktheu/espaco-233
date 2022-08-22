﻿# The script of the game goes in this file.

# Definindo os personagens
define e = Character("Eileen")
define s = Character("ESMAUGUE", color="#ed5a64")

# Minha localização atual
define cur_location = ""

# Início do Jogo

label start:

    scene bg room

    show eileen happy

    "Medo do esmaugyee"
    s "{b}RAAAAURRRRR{/b}"

    menu:
        "QUAL DIREÇÃO?"

        "DIREITA":
            python:
                goto_store.go_to_right(cur_location)
        "ESQUERDA":
            python:
                goto_store.go_to_left(cur_location)
        "CIMA":
            python:
                goto_store.go_to_up(cur_location)
        "BAIXO":
            python:
                goto_store.go_to_down(cur_location)


    return
