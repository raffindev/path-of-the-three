from random import randint

# Dado 4 lados - usado para DROP e DANO de ARMAS FRACAS
def d4():
    return randint(1, 4)

# Dado 6 lados - usado para ação de DANO de ARMAS MÉDIAS
def d6():
    return randint(1, 6)

# Dado 8 lados - usado para ação de DANO de ARMAS FORTES - usado para DEFESA tambem
def d8():
    return randint(1, 8)

# Dado 12 lados - usado para CALCULAR ATAQUE
def d12():
    return randint(1, 12)    

# Dado 20 lados - usado para CALCULAR ATAQUE
def d20():
    return randint(1, 20)    