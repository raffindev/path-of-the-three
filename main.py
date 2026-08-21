# Teste de fluxo de ataque.

from personagens.herois import grupo_herois
from personagens.monstros import tipos_monstros, goblin, slime
from combate.ações import gerar_encontro, defender, curar
from combate.batalha import turno_heroi, iniciar_batalha, batalha, turno_monstros
from itens.mochilas import mochilas

monstros_batalha = iniciar_batalha(grupo_herois, tipos_monstros)

batalha(grupo_herois, monstros_batalha, mochilas)
