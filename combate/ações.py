from combate.dados import d6, d8, d12
from itens.itens import poção_de_cura
from random import choice, randint

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
def escolher_acao():
    print('''
    1 - Atacar
    2 - Defender
    3 - Curar
    4 - Fugir
    ''')

    escolha_acao = input('Qual será seu próximo movimento: ')
    return escolha_acao

# Função Escolher Alvo
def escolher_alvo(monstros_batalha):
    print('='*5, 'INIMIGOS', '='*5,'\n') 
    for i, monstro in enumerate(monstros_batalha, start=1):
        print(f'{i} - {monstro["Nome"]}')

    grupo_monstro = int(input('\nEscolha seu Alvo: '))
    if 1 <= grupo_monstro <= len(monstros_batalha):
        monstro_alvo = monstros_batalha[grupo_monstro - 1]
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
        print(f'PV: {alvo["Pontos de Vida Atual"]} / {alvo["Pontos de Vida Maxima"]}')
        if alvo["Pontos de Vida Atual"] <= 0:
            alvo["Pontos de Vida Atual"] = 0
            print(f'{alvo["Nome"]} derrotado.')
            
    else:
        print('Ataque errou')

def defender(heroi):
    print(f'\n{heroi["Nome"]} escolheu defender.')

    bonus_defesa = d8()

    print(f'Rolando d8: Você tirou... {bonus_defesa}')
    defesa_base = heroi["Defesa"] + heroi["Classe de Armadura"]
    print(f'Heroi tem {defesa_base} de defesa base + bonus de defesa de: {bonus_defesa}')
    defesa_temporaria = defesa_base + bonus_defesa
    print(f'A defesa temporaria do heroi ficou: {defesa_temporaria}')

    return defesa_temporaria

def curar(heroi):
    print(f'{heroi["Nome"]} PV: {heroi["Pontos de Vida Atual"]} / {heroi["Pontos de Vida Maxima"]}')
    if heroi["Poções"] == 0:
        print("Impossivel curar, o numero de poções é 0.")

    else:
        if heroi["Pontos de Vida Atual"] == heroi["Pontos de Vida Maxima"]:
            print("Heroi com vida maxima, não é possivel utilizar o item.")

        else:
            dano_recebido = heroi["Pontos de Vida Maxima"] - heroi["Pontos de Vida Atual"]
            print(f'{poção_de_cura["Nome"]}: {poção_de_cura["Cura"]}')
            if dano_recebido < poção_de_cura["Cura"]:
                cura = dano_recebido
            else:
                cura = poção_de_cura["Cura"]

            heroi["Pontos de Vida Atual"] += cura
            heroi["Poções"] -= 1  
            print(f"Recuperou {cura} PV")
            print(F'PV {heroi["Pontos de Vida Atual"]} / {heroi["Pontos de Vida Maxima"]}:')