transform aiden_bounce2:
    xalign 1.2 yalign 0.45
    linear 0.5 yalign 0.0
    linear 1.0 yalign 0.45
    repeat

transform loren_left:
    xalign 1.2 yalign 0.65

label chapter3:

    stop sound

    # $ decompress("loren")
    $ decompress("aiden")
    $ compress("buttons", "button_", 8)


    image b_central = im.Scale("images/bg ship_3.png", 1920, 1080)
    image aiden_lidle = im.Scale("images/aiden_2.png", 1000, 1000)
    image aiden_lworried = im.Scale("images/aiden_3.png", 1000, 1000)

    scene b_central with fade

    "Após todo o sufoco e determinação de Loren ela consegue consertar todos os defeitos encontrados na nave e sua esperança é finalmente restaurada, ela corre alegremente pelos corredores, pulando e saltitando pra lá e pra cá."

    play sound "sfxs/voice/risada.ogg" volume 0.95

    l "Finalmente, meu deus, como foi difícil, mas até que enfim, vou poder voltar a dormir e VIVER, AEEEEE CARA..."

    show aiden_lidle at aiden_bounce2 with fade
    i "Senhorita Loren!"

    l "Oi Aiden fala meu chapa, vai me botar pra mimir finalmente, já está batendo a saudades, eu sei eu sei, eu vou sentir saudades também meu querido."

    hide aiden_lidle
    show aiden_lworried at aiden_bounce2
    i "Não é isso, mas eu receio que não acabou."

    play sound "sfxs/voice/duvida.ogg" volume 1.0

    l "NÃO ACABOU? Mas você disse que só tinham 3 problemas na nave, e agora não acabou?"

    i "Me desculpe, até aquele momento eu achava que só existiam aqueles defeitos, mas como o sistema estava danificado, eu não consegui identificar todos eles."

    play sound "sfxs/voice/resmungo.ogg" volume 1.0

    l "DROGA!"

    l "Qual é o problema? Se for urgente me diz logo."

    hide aiden_lworried
    show aiden_lidle at aiden_bounce2
    i "Pelo jeito um dos tanques reservas está com um vazamento, e como é pequeno por isso não foi perceptível para mim sem a ajuda do sistema."

    i "Mas por conta de todo o tempo que estamos arrumando as outras partes da nave, o combustível já está quase acabando nesse tanque, e com isso se ele se esgotar eu não conseguirei te pôr novamente em sua cabine."

    play sound "sfxs/voice/resmungo.ogg" volume 1.0

    l "QUAL É UNIVERSO, beleza deixa eu ir logo."

    # $ compress("loren", "loren_", 1)
    $ compress("aiden", "aiden_", 4)
    jump chapter4

    return
