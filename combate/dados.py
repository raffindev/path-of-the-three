from random import randint

# Dado 4 lados - usado para drop
def d4():
    return randint(1, 4)

# Dado 6 lados - usado para ação ataque
def d6():
    return randint(1, 6)