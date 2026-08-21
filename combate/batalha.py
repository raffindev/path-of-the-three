from combate.ações import escolher_ação, escolher_alvo, gerar_encontro
from combate.ações import atacar, defender, curar, fugir, drop_item
from itens.mochilas import mochilas
from utils.validações import cabeçalho
from random import choice
import time

# Estrutura início da batalha
def iniciar_batalha(herois, monstros_disponiveis):

    monstros_batalha = gerar_encontro(monstros_disponiveis)
    print(cabeçalho("BATALHA"))

    print("\nHeróis:")
    for i, heroi in enumerate(herois, start=1):
        print(f'{i} - {heroi["Nome"]}')

    print('\n⚔️  A batalha começou!')

    return monstros_batalha

# Estrutura de batalha - Turno do heroi
def turno_heroi(heroi, monstros_batalha, mochilas):

    time.sleep(0.5)
    print(f'\n⚔️  TURNO DE {heroi["Nome"].upper()}')
    ação = escolher_ação()

    if ação == "1":
        print("\n⚔️  Ação escolhida: Atacar")
        numero, alvo = escolher_alvo(monstros_batalha)
        atacar(heroi, alvo)

    elif ação == "2":
        print("\n🛡️  Ação escolhida: Defender")
        defesa_temporaria = defender(heroi)
        return "defesa", defesa_temporaria

    elif ação == "3":
        print("\n❤️  Ação escolhida: Curar")
        curar(heroi, mochilas)

    elif ação == "4":
        print("\n🏃 Ação escolhida: Fugir")

        if fugir(heroi):
            return "fugiu"

# Turno dos monstros
def turno_monstros(monstros_batalha, herois):
    time.sleep(0.5)

    print('\n👹 Os monstros se preparam para atacar!')

    for monstro in monstros_batalha:
        if monstro["Pontos de Vida Atual"] > 0:
            print(f'\n👹 TURNO DO {monstro["Nome"].upper()}')
            herois_vivos = [
                heroi
                for heroi in herois
                if heroi["Pontos de Vida Atual"] > 0
            ]

            heroi_alvo = choice(herois_vivos)
            atacar(monstro, heroi_alvo)
            resultado = verificar_batalha(herois, monstros_batalha)
            if resultado != "continua":
                break

# Verificar se ainda esta batalhando
def verificar_batalha(herois, monstros_batalha):

    vitoria = all(monstro["Pontos de Vida Atual"] == 0 for monstro in monstros_batalha)
    derrota = all(heroi["Pontos de Vida Atual"] == 0 for heroi in herois)

    if vitoria:
        print(cabeçalho("VITÓRIA"))
        print("🏆 Todos os inimigos foram derrotados!")
        print("Vocês venceram a batalha!")
        return "vitoria"

    if derrota:
        print(cabeçalho("DERROTA"))
        print("💀 Todos os heróis foram derrotados.")
        print("A aventura termina aqui.")
        return "derrota"

    return "continua"

# Fluxo da batalha
def batalha(herois, monstros_batalha, mochilas):

    while True:
        herois_defendendo = []

        # Turno dos heróis
        for heroi in herois:
            if heroi["Pontos de Vida Atual"] > 0:
                resultado_turno = turno_heroi(heroi, monstros_batalha, mochilas)
                if resultado_turno == "fugiu":
                    return
                if resultado_turno and resultado_turno[0] == "defesa":
                    defesa_original = heroi["Defesa"]
                    heroi["Defesa"] = resultado_turno[1]
                    herois_defendendo.append((heroi, defesa_original))

                resultado = verificar_batalha(herois, monstros_batalha)
                if resultado == "vitoria":
                    for monstro in monstros_batalha:
                        drop_item(monstro, mochilas)
                    return
                if resultado == "derrota":
                    return

        # Turno dos monstros
        turno_monstros(monstros_batalha, herois)
        resultado = verificar_batalha(herois, monstros_batalha)
        if resultado == "vitoria":
            for monstro in monstros_batalha:
                drop_item(monstro, mochilas)
            return
        if resultado == "derrota":
            return

        # Remove a defesa temporária
        for heroi, defesa_original in herois_defendendo:
            heroi["Defesa"] = defesa_original