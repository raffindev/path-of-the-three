from combate.ações import escolher_ação, escolher_alvo, gerar_encontro
from combate.ações import atacar, defender, curar, fugir, drop_item
from random import choice

# Estrutura inicio da batalha
def iniciar_batalha(herois, monstros_disponiveis):
    monstros_batalha = gerar_encontro(monstros_disponiveis)
    print('')
    print('='*5, 'BATALHA', '='*5)

    for i, heroi in enumerate(herois, start=1):
        print(f'{i} - {heroi["Nome"]}')
    print(f'A batalha começou!')

    return monstros_batalha

# Estrutura de batalha - Turno do heroi
def turno_heroi(heroi, monstros_batalha):
    print(f'\nTurno do {heroi["Nome"]}')
    ação = escolher_ação()

    if ação == "1":
        print("\nAção escolhida: 1 - Atacar")
        
        numero, alvo = escolher_alvo(monstros_batalha)
        atacar(heroi, alvo)

    elif ação == "2":
        defender(heroi)

    elif ação == "3":
        curar(heroi)

    elif ação == "4":
        fugir(heroi)

# Turno dos monstros
def turno_monstros(monstros_batalha, herois):
    for monstro in monstros_batalha:
        if monstro["Pontos de Vida Atual"] > 0:
            print(f'\nTurno do {monstro["Nome"]}')
            herois_vivos = [heroi for heroi in herois if heroi["Pontos de Vida Atual"] > 0]
            heroi_alvo = choice(herois_vivos)
            atacar(monstro, heroi_alvo)
            resultado = verificar_batalha(herois, monstros_batalha)
            if resultado != "continua":
                break

# Verificar se ainda esta batalhando
def verificar_batalha(herois, mostros_batalha):
    vitoria = all(monstro["Pontos de Vida Atual"] == 0 for monstro in mostros_batalha)
    derrota = all(heroi["Pontos de Vida Atual"] == 0 for heroi in herois)
    if vitoria:
        print('Vitória, Vocês venceram')
        return "vitoria"
    elif derrota:
        print('infelizmente todos heróis morreram')
        return "derrota"
    else:
        print('A batalha continua')
        return "continua"

# fluxo da batalha
def batalha(herois, monstros_batalha, mochilas):
    while True:
        for heroi in herois:
            if heroi["Pontos de Vida Atual"] > 0:
                turno_heroi(heroi, monstros_batalha)
                resultado = verificar_batalha(herois, monstros_batalha)
                if resultado == "vitoria":
                    for monstro in monstros_batalha:
                        drop_item(monstro, mochilas)
                    return

                if resultado == "derrota":
                    return

        resultado = verificar_batalha(herois, monstros_batalha)
        if resultado != 'continua':
            break
        
        turno_monstros(monstros_batalha, herois)
        resultado = verificar_batalha(herois, monstros_batalha)
        if resultado == "vitoria":
            for monstro in monstros_batalha:
                drop_item(monstro, mochilas)
            return

        if resultado == "derrota":
            return
    