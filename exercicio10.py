#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:32:43 2022

@author: isaacnilberto
"""
from random import randint
itens = ('pedra','papel','tesoura')
computador = randint(0,2)

pergunta_jogador1 = print("""
[0]. pedra?
[1]. papel?
[2]. tesoura?

Jogador 1 digite: 
""")
jogador = int(input('Qual sua jogada°? '))
print('='*10)
print(f'jogador jogou {itens[jogador]}, O computador {itens[computador]}')
print('='*10)

if computador == 0:
    if jogador == 0:
        print('empate.')
    elif jogador == 1:
        print('Jogador ganhou.')
    elif jogador == 2:
        print('Computador ganhou.')
    else:
        print('jogada invalida')
elif computador ==1 :
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('empate 1 ganhou')
    elif jogador == 2:
        print('jogador ganhou')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('jogador ganhou')
    elif jogador == 1:
        print('computador ganhou 1 ganhou')
    elif jogador == 2:
        print('empate ganhou')
    else:
        print('jogada invalida')