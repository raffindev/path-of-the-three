# Teste de fluxo de ataque.

from personagens.herois import guerreiro
from personagens.monstros import goblin
from combate.ações import atacar
from personagens.monstros import tipos_monstros
from combate.ações import gerar_encontro
from combate.ações import escolher_alvo

monstros = gerar_encontro(tipos_monstros)
print("\n")
numero, alvo = escolher_alvo(monstros)

print(f'\nVocê escolheu: {alvo["Nome"]} {numero}\n')
atacar(guerreiro, alvo)