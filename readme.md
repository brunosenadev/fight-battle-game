
# Jogo de Batalha em Turnos

Este é um projeto de estudo focado em programação orientada a objetos (POO), implementando um jogo de luta em turnos. O jogador controla um herói, enquanto o inimigo é controlado pela máquina. O objetivo é reduzir a vida do oponente a zero utilizando ataques normais e habilidades especiais.

## Conceitos Principais

- **Herói:** O jogador controla o herói, que tem uma habilidade especial limitada por cargas.
- **Inimigo:** A máquina controla o inimigo, que possui um tipo específico e faz ataques no seu turno.
- **Turnos:** O jogo é baseado em turnos alternados, onde cada jogador ataca baseado no seu nível até que a vida do oponente chegue a zero.
- **Vencedor**: Ganha o jogador que conseguir reduzir a vida do oponente a zero primeiro.
## Estrutura do Jogo

#### O herói possui:
- Pontos de vida.
- Nível.
- Ataque normal.
- Ataque especial.

#### O inimigo possui:
- Pontos de vida.
- Nível.
- Tipo.
- Ataque normal.

## Tecnologias e Dependências

Este projeto foi implementado apenas com Python. A única dependência externa é a biblioteca padrão random, usada para controlar o valor do dano tanto do herói quanto do oponente.
## Instalação e Execução

#### Pré-requisitos:
- Python 3.x

#### Como rodar o jogo:

**1.** Clone o repositório para sua máquina local:
```
    git clone https://github.com/brunosenadev/fight-battle-game.git
    cd fight-battle-game
```
**2.** Execute o jogo:
```
    python game.py
```

O jogo será executado no terminal, onde o jogador pode escolher entre ataque normal e ataque especial, enquanto o inimigo é controlado automaticamente.

#### Exemplo de jogo:
```
Starting battle!

Character Details:
Name: Ares
Life: 100
Level: 5
Power: Super Strength


Name: Dragon
Life: 100
Level: 5
Type: Mythical

Press enter to attack...
Choose (1 - Normal Attack, 2 - Power [2 charges remaining] ): 1
Ares attacked Dragon and dealt 18 damage.
Dragon attacked Ares and dealt 16 damage.

Character Details:
Name: Ares
Life: 84
Level: 5
Power: Super Strength


Name: Dragon
Life: 82
Level: 5
Type: Mythical

Press enter to attack...
```
O jogo continua até que um dos personagens tenha sua vida reduzida a zero.
## Objetivo Educacional

Este projeto foi criado com o intuito de estudar e aplicar conceitos de ***programação orientada a objetos*** em Python. O foco está em:

- Definição de classes e objetos (Herói, Inimigo, etc.).
- Uso de herança, encapsulamento e polimorfismo.
- Controle de fluxo com loops e condições.
- Simulação de comportamento controlado por máquina.
