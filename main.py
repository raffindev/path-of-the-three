# Teste de fluxo de ataque.

from personagens.herois import guerreiro
from personagens.monstros import tipos_monstros
from combate.ações import gerar_encontro
from combate.batalha import turno_heroi


monstros = gerar_encontro(tipos_monstros)

turno_heroi(guerreiro, monstros)