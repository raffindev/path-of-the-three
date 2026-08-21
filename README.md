# RPG Python - PATH OF THE THREE

Um RPG de combate em terminal desenvolvido em Python.

O projeto acompanha um grupo de aventureiros formado por um Guerreiro, um Arqueiro e um Ranger, enfrentando criaturas que surgem pelo caminho através de batalhas por turnos baseadas em rolagens de dados.

O objetivo do projeto é evoluir gradualmente um sistema de RPG, começando por combates simples e expandindo futuramente para novas mecânicas, inimigos, equipamentos, exploração e progressão do jogador.

## Funcionalidades atuais

* Combate por turnos
* Sistema de ações:

  * Atacar
  * Defender
  * Curar
  * Fugir
* Sistema de rolagem de dados
* Dados D4, D6, D8, D12 e D20
* Múltiplos personagens jogáveis
* Inimigos gerados aleatoriamente
* Escolha de alvos durante o combate
* Sistema de defesa temporária
* Sistema de cura
* Sistema de fuga
* Sistema de drops
* Drops distribuídos aleatoriamente entre os heróis
* Sistema de itens
* Mochilas individuais para os heróis
* Controle de quantidade de itens
* Condições de vitória e derrota
* Encerramento da batalha ao fugir
* Validação de entradas do jogador
* Tratamento de entradas inválidas
* Mensagens personalizadas para as ações de combate
* Cabeçalhos padronizados no terminal
* Pausas com `time.sleep()` para melhorar o ritmo das batalhas

## Estrutura do projeto

```text
path-of-the-three/
│
├── main.py
│
├── personagens/
│   ├── herois.py
│   └── monstros.py
│
├── combate/
│   ├── ações.py
│   ├── batalha.py
│   └── dados.py
│
├── itens/
│   ├── itens.py
│   └── mochilas.py
│
└── utils/
    └── validações.py
```

## Objetivos do projeto

* Praticar lógica de programação
* Aprender organização de projetos
* Aplicar modularização de código
* Trabalhar com funções
* Trabalhar com listas e dicionários
* Trabalhar com persistência e estruturas de dados
* Desenvolver tratamento e validação de entradas
* Desenvolver boas práticas de programação
* Construir um projeto para portfólio

## Futuras expansões

* Novos inimigos
* Novas armas
* Novos itens
* Inventário expandido
* Exploração
* Novos tipos de encontro
* Chefes
* Sistema de progressão
* Experiência e níveis
* Habilidades especiais
* Sistema de status
* Melhorias na interface do terminal
* Animações e efeitos no terminal