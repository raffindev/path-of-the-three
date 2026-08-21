from combate.dados import d4, d6, d8, d12, d20
from itens.itens import poção_de_cura
from itens.mochilas import mochilas
from utils.validações import cabeçalho, validar_ação
from random import choice, randint
import time

# Função Gerar encontro.
def gerar_encontro(monstros_disponiveis):

    quantidade_monstros = randint(1, 4)
    monstro_escolhido = choice(monstros_disponiveis)
    nome_monstro = monstro_escolhido["Nome"]

    if quantidade_monstros > 1:
        nome_monstro += "s"

    monstros_batalha = []

    for _ in range(quantidade_monstros):
        monstros_batalha.append(monstro_escolhido.copy())

    print(cabeçalho("ENCONTRO"))
    print(f'\n⚠️  {quantidade_monstros} {nome_monstro} surgiram!')
    print('Preparem-se para a batalha!\n')

    print(cabeçalho("INIMIGOS"))
    print()

    for i, monstro in enumerate(monstros_batalha, start=1):
        print(f'{i} - {monstro["Nome"]}')

    return monstros_batalha

# Função Definir Ação.
def escolher_ação():

    while True:

        print(cabeçalho("AÇÕES"))
        print("\n1 - Atacar")
        print("2 - Defender")
        print("3 - Curar")
        print("4 - Fugir")

        escolha_ação = input("\nQual será seu próximo movimento: ")

        if validar_ação(escolha_ação):
            return escolha_ação

        print('\n❌ Ação inválida!')
        print('⚔️ Escolha uma opção entre 1 e 4.')
        time.sleep(0.8)

# Função Escolher Alvo.
def escolher_alvo(monstros_batalha):

    monstros_vivos = [monstro for monstro in monstros_batalha if monstro["Pontos de Vida Atual"] > 0]

    print(cabeçalho("INIMIGOS"))
    print()

    for i, monstro in enumerate(monstros_vivos, start=1):
        print(f'{i} - {monstro["Nome"]}')

    while True:
        try:
            grupo_monstro = int(input('\nEscolha seu alvo: '))
            if 1 <= grupo_monstro <= len(monstros_vivos):
                monstro_alvo = monstros_vivos[grupo_monstro - 1]
                print(f'\n🎯 Alvo escolhido: {monstro_alvo["Nome"]} {grupo_monstro}')
                return grupo_monstro, monstro_alvo

            print('⚠️ Alvo inválido!')
        except ValueError:
            print('❌ Movimento inválido!')
            print('⚔️ Escolha um dos inimigos apresentados pelo número.')

# Função Atacar.
def atacar(atacante, alvo):

    print(f'\n⚔️  {atacante["Nome"]} ataca {alvo["Nome"]}!')
    print(
        f'Força: {atacante["Força"]} | '
        f'Dano da arma: {atacante["Dano da Arma"]}'
    )

    print('\n🎲 Rolando D12...')
    time.sleep(0.8)
    rolar_d12 = d12()
    print(f'🎲 Resultado: {rolar_d12}')

    poder_de_ataque = (
        atacante["Força"]
        + atacante["Dano da Arma"]
        + rolar_d12
    )
    print(f'⚔️  Poder de ataque: {poder_de_ataque}')

    defesa_total = alvo["Defesa"] + alvo["Classe de Armadura"]
    print(f'🛡️  Defesa de {alvo["Nome"]}: {defesa_total}')
    if poder_de_ataque >= defesa_total:

        print('\n💥 Ataque acertou!')
        print('🎲 Calculando o dano...')
        time.sleep(0.5)

        print('🎲 Rolando D6...')
        time.sleep(0.8)
        rolar_d6 = d6()
        print(f'🎲 Resultado: {rolar_d6}')

        calculo_dano = atacante["Dano da Arma"] + rolar_d6
        print(
            f'⚔️  Dano da arma: {atacante["Dano da Arma"]} '
            f'+ D6: {rolar_d6} '
            f'= {calculo_dano} de dano'
        )

        alvo["Pontos de Vida Atual"] -= calculo_dano
        print(f'\n💥 {alvo["Nome"]} sofreu {calculo_dano} de dano.')

        if alvo["Pontos de Vida Atual"] <= 0:
            alvo["Pontos de Vida Atual"] = 0
            print(f'💀 {alvo["Nome"]} foi derrotado!')

        print(
            f'❤️  PV: {alvo["Pontos de Vida Atual"]} '
            f'/ {alvo["Pontos de Vida Maxima"]}\n'
        )

    else:
        print('\n❌ ATAQUE ERROU!')

# Função Defender.
def defender(heroi):

    print(f'\n🛡️  {heroi["Nome"]} escolheu defender.\n')

    print('🎲 Rolando D8 para determinar o bônus de defesa...')
    time.sleep(0.8)
    bonus_defesa = d8()
    print(f'🎲 Resultado: {bonus_defesa}')

    defesa_base = heroi["Defesa"] + heroi["Classe de Armadura"]

    defesa_temporaria = defesa_base + bonus_defesa

    print(f'🛡️  Defesa base: {defesa_base}')
    print(f'✨ Bônus de defesa: +{bonus_defesa}')
    print(f'🛡️  Defesa durante este turno: {defesa_temporaria}')

    return defesa_temporaria

# Função Curar.
def curar(heroi, mochilas):

    mochila_heroi = mochilas[heroi["Nome"]]
    quantidade_pocoes = mochila_heroi["Poção de Cura"]

    if quantidade_pocoes <= 0:
        print(f'\n⚠️  {heroi["Nome"]} não possui Poção de Cura!\n')
        return

    if heroi["Pontos de Vida Atual"] == heroi["Pontos de Vida Maxima"]:
        print(f'\n❤️  {heroi["Nome"]} já está com os PV máximos!')
        print('🧪 A Poção de Cura não foi consumida.\n')
        return

    cura = 20
    heroi["Pontos de Vida Atual"] += cura
    if heroi["Pontos de Vida Atual"] > heroi["Pontos de Vida Maxima"]:
        heroi["Pontos de Vida Atual"] = heroi["Pontos de Vida Maxima"]

    mochila_heroi["Poção de Cura"] -= 1

    print(f'\n❤️  {heroi["Nome"]} usou uma Poção de Cura!')
    print(f'❤️  PV: {heroi["Pontos de Vida Atual"]} / {heroi["Pontos de Vida Maxima"]}')
    print(f'🎒  Poções restantes: {mochila_heroi["Poção de Cura"]}\n')

# Função Fugir.
def fugir(heroi):

    print(f'\n🏃 {heroi["Nome"]} tentou escapar do combate...')
    time.sleep(0.5)

    print('🎲 O destino foi lançado...')
    time.sleep(1)

    chance_fugir = d12()
    print(f'Resultado: {chance_fugir}')

    if chance_fugir >= 9:
        print(f'\n💨 {heroi["Nome"]} encontrou uma abertura e conseguiu escapar!')
        print('A batalha foi encerrada.')
        return True

    print(f'\n⚔️  {heroi["Nome"]} não conseguiu escapar!')
    print('Os inimigos fecharam o caminho. A batalha continua...')
    return False

# Função drop de item.
def drop_item(monstro, mochilas):

    nome_monstro = monstro["Nome"]
    item = monstro["Drop"]
    chance_drop_base = monstro["Drop Porcentagem"]

    print(f'\n🎁 Recompensa de {nome_monstro}')
    print(f'Chance base de drop: {chance_drop_base}%')
    print('\n🎲 Rolando D4 para determinar o bônus de drop...')
    time.sleep(0.8)

    rolar_d4 = d4()

    print(f'🎲 Resultado: {rolar_d4}')

    bonus_drop = rolar_d4 * 25
    chance_drop = chance_drop_base + (chance_drop_base * bonus_drop / 100)
    print(f'Chance final de {item}: {chance_drop}%')
    print('\n🎲 Rolando D20 para verificar o drop...')
    time.sleep(1)

    rolar_d20 = d20()
    print(f'🎲 Resultado: {rolar_d20}')
    porcentagem_drop = rolar_d20 * 5

    if porcentagem_drop <= chance_drop:
        heroi = choice(list(mochilas.keys()))
        mochilas[heroi][item] += 1

        print(f'\n🎉 DROP CONFIRMADO!')
        print(f'{item} encontrado!')
        print(f'🎒 O item foi enviado para a mochila de {heroi}.')

    else:
        print('\n🍃 A sorte não estava ao lado de vocês...')
        print('Nenhum item foi encontrado.')