# História principal e desenvolvimento do jogo

from personagens.herois import grupo_herois
from personagens.monstros import tipos_monstros
from combate.batalha import iniciar_batalha, batalha
from itens.mochilas import mochilas


monstros_batalha = iniciar_batalha(grupo_herois, tipos_monstros)

batalha(grupo_herois, monstros_batalha, mochilas)

print('\n' + '=' * 40)
print('Obrigado por jogar!'.center(40))
print('Até a próxima aventura!'.center(40))
print('=' * 40)