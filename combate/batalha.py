from combate.ações import escolher_ação, escolher_alvo, atacar, defender, curar, fugir

# Estrutura de batalha - Turno do heroi
def turno_heroi(heroi, monstros_batalha):
    print(f'\nTurno do {heroi["Nome"]}')
    ação = escolher_ação()

    if ação == "1":
        print("\nAção escolhida: 1 - Atacar")
        
        numero, alvo = escolher_alvo(monstros_batalha)
        atacar(heroi, alvo)

    elif ação == "2":
        defender(heroi)

    elif ação == "3":
        curar(heroi)

    elif ação == "4":
        fugir(heroi)