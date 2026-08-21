from combate.ações import escolher_acao, escolher_alvo, atacar, defender, curar

# Estrutura de batalha - Turno do heroi
def turno_heroi(heroi, monstros_batalha):
    print(f'\nTurno do {heroi["Nome"]}')
    acao = escolher_acao()

    if acao == "1":
        print("\nAção escolhida: 1 - Atacar")
        
        numero, alvo = escolher_alvo(monstros_batalha)
        atacar(heroi, alvo)

    elif acao == "2":
        defender(heroi)

    elif acao == "3":
        curar(heroi)