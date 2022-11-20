label puzzle2:

    call steps

    scene black with fade

    if puzzle2_completed == False:
        jump intro_puzzle2
    else:
        call screen buttons_navigation (True, False, False, False)

return

label intro_puzzle2:
    scene black with fade

    i "Parece que o sistema de gravidade dessa sala de armazéns está desativado, que tal a senhorita tentar consertá-lo?"

    i "A alavanca está localizada logo a sua frente, no fim da sala."

    i "Aconselho a ter cuidado com as caixas e itens espalhados por aí."

    menu:
        "Tentar chegar ao fim da sala?"

        "SIM":
            jump do_puzzle2
        "NÃO":
            jump central

    return


label do_puzzle2:
    scene black with fade

    menu:
        "Uma caixa está vindo em sua direção!"

        "Desviar para a esquerda":
            l "Um pouco fácil."

        "Desviar para a direita":
            jump intro_puzzle2

    scene black with fade
    menu:
        "Um armário grande está se aproximando!"

        "Ir para baixo":
            l "Ufa! Essa foi por pouco..."

        "Ir para cima":
            jump intro_puzzle2


    scene black with fade
    menu:
        "Uma gaveta cheia de pregos começa a chegar perto!"

        "Correr":
            jump intro_puzzle2

        "Desviar para a direita":
            $ puzzle2_completed = True
            l "Pregos?! Tá de brincadeira comigo..."

    "Loren chega ao final da sala, conseguindo então apertar o botão e ativar o sistema de gravidade novamente."

    jump central

    return
