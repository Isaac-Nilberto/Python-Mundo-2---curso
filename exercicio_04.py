#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:35:33 2022

@author: isaacnilberto
"""

"""
Questão 4:
Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo de alistamento.
seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
nascimento = int(input('Qual seu ano de nascimento? (in YYYY) '))

atual = date.today().year

idade = atual - nascimento

print(f'Sua idade é {idade}.')
if idade == 18:
    print('Você tem que se alistar.')

elif idade < 18:
    saldo = 18 - idade
    print(f'Voce ainda vai se alistar. Faltam {saldo} anos')
    ano = atual + saldo
    print(f'Seu alistamento será {ano}.')
else:
    saldo = idade - 18
    print(f'Voce já deveria ter se alistado passou {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi {ano}.')