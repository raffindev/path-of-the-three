from combate.dados import d4, d6, d8, d12, d20
from itens.itens import poção_de_cura
from itens.mochilas import mochilas
from random import choice, randint

def cabeçalho(txt):
    return '='*40 + '\n' + txt.center(40) + '\n' + '='*40

# Função Gerar encontro
def gerar_encontro(monstros_disponiveis):
    quantidade_monstros = randint(1, 4)
    monstro_escolhido = choice(monstros_disponiveis)
    print(f'Apareceu {quantidade_monstros} {monstro_escolhido["Nome"]}. CUIDADO!!!\n')
    monstros_batalha = []
    for _ in range(quantidade_monstros):
        monstros_batalha.append(monstro_escolhido.copy())

    for i, monstro in enumerate(monstros_batalha, start=1):
        print(f'{monstro["Nome"]} {i} | ', end= '')

    return monstros_batalha

# Função Definir Ação
def escolher_ação():
    print('''
    1 - Atacar
    2 - Defender
    3 - Curar
    4 - Fugir
    ''')

    escolha_ação = input('Qual será seu próximo movimento: ')
    return escolha_ação

# Função Escolher Alvo
def escolher_alvo(monstros_batalha):
    monstros_vivos = [monstro for monstro in monstros_batalha if monstro["Pontos de Vida Atual"] > 0]

    print('=' * 5, 'INIMIGOS', '=' * 5, '\n')
    for i, monstro in enumerate(monstros_vivos, start=1):
        print(f'{i} - {monstro["Nome"]}')
    grupo_monstro = int(input('\nEscolha seu Alvo: '))

    if 1 <= grupo_monstro <= len(monstros_vivos):
        monstro_alvo = monstros_vivos[grupo_monstro - 1]
        print(f'\nAlvo escolhido: {monstro_alvo["Nome"]} {grupo_monstro}')
        return grupo_monstro, monstro_alvo

    print('Alvo inválido!')

# Função atacar
def atacar(atacante, alvo):
    print(f'\nO {atacante["Nome"]} tem: Força: {atacante["Força"]} - Dano da Arma: {atacante["Dano da Arma"]}')
    rolar_d12 = d12()
    print(f'Rolando o dado d12: Você tirou... {rolar_d12}')
    poder_de_ataque = atacante["Força"] + atacante["Dano da Arma"] + rolar_d12
    print(f'Seu poder de ataque nesse turno foi de {poder_de_ataque}')

    defesa_total = alvo["Defesa"] + alvo["Classe de Armadura"]
    print(f'\nA defesa do {alvo["Nome"]} é {defesa_total}')

    if poder_de_ataque >= defesa_total:
        print('Ataque acertou!, vamos para o calculo de dano:')
        rolar_d6 = d6()
        print(f'\nRolando dado d6: Você tirou... {rolar_d6}')
        calculo_dano = atacante["Dano da Arma"] + rolar_d6
        print(f'Somando o dano da arma: {atacante["Dano da Arma"]} + o d6: {rolar_d6} seu dano foi de: {calculo_dano}')
        alvo["Pontos de Vida Atual"] -= calculo_dano
        print(f'\n{alvo["Nome"]} sofreu {calculo_dano} de dano.')
        if alvo["Pontos de Vida Atual"] <= 0:
            alvo["Pontos de Vida Atual"] = 0
            print(f'{alvo["Nome"]} derrotado.')
        print(f'PV: {alvo["Pontos de Vida Atual"]} / {alvo["Pontos de Vida Maxima"]}')
            
    else:
        print('Ataque errou')

# Função Defender
def defender(heroi):
    print(f'\n{heroi["Nome"]} escolheu defender.')

    bonus_defesa = d8()

    print(f'Rolando d8: Você tirou... {bonus_defesa}')
    defesa_base = heroi["Defesa"] + heroi["Classe de Armadura"]
    print(f'Heroi tem {defesa_base} de defesa base + bonus de defesa de: {bonus_defesa}')
    defesa_temporaria = defesa_base + bonus_defesa
    print(f'A defesa temporaria do heroi ficou: {defesa_temporaria}')

    return defesa_temporaria

# Função Curar 
def curar(heroi, mochilas):
    mochila_heroi = mochilas[heroi["Nome"]]
    quantidade_pocoes = mochila_heroi["Poção de Cura"]

    if quantidade_pocoes > 0:
        cura = 20
        heroi["Pontos de Vida Atual"] += cura

        if heroi["Pontos de Vida Atual"] > heroi["Pontos de Vida Maxima"]:
            heroi["Pontos de Vida Atual"] = heroi["Pontos de Vida Maxima"]
        mochila_heroi["Poção de Cura"] -= 1

        print(f'{heroi["Nome"]} usou uma Poção de Cura!')
        print(f'PV: {heroi["Pontos de Vida Atual"]} / {heroi["Pontos de Vida Maxima"]}')
        print(f'Poções restantes: {mochila_heroi["Poção de Cura"]}')
    else:
        print(f'{heroi["Nome"]} não possui Poção de Cura!')

# Função Fugir.
def fugir(heroi):
    print(f'{heroi["Nome"]} tentou fugir...')
    chance_fugir = d12()
    print(f'Rolando d12...')
    print(f'Você tirou {chance_fugir}.')
    return chance_fugir >= 9

# Drop de item
def drop_item(monstro, mochilas):
    print(f'{monstro["Nome"]} tem {monstro["Drop Porcentagem"]} % de chance de drop.')
    chance_drop_base = monstro["Drop Porcentagem"]

    print('Rolando um D4 para determinar sua taxa de drop...')
    rolar_d4 = d4()
    print(f'Você tirou {rolar_d4} no dado!')

    bonus_drop = rolar_d4 * 25
    chance_drop = chance_drop_base + (chance_drop_base * bonus_drop / 100)
    print(f'Sua chance de dropar {monstro["Drop"]} é de {chance_drop}%!')

    rolar_d20 = d20()
    print(f'Você tirou {rolar_d20} no dado!')
    porcentagem_drop = rolar_d20 * 5

    if porcentagem_drop <= chance_drop:
        heroi = choice(list(mochilas.keys()))
        mochilas[heroi][monstro["Drop"]] += 1
        print(f'Drop confirmado! Você conseguiu {monstro["Drop"]}!')
        print(f'O item foi para a mochila de {heroi}.')
    else:
        print('💀 O drop não veio dessa vez...')