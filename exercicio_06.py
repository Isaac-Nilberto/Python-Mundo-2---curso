#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:08:04 2022

@author: isaacnilberto
"""

'''
A confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre a sua categoria, de acordo com a sua idade:
- até 9 anos: mirim.
- até 14 anos: infantil.
- até 19 anos: júnior.
- até 20 anos: sênior.
- acima: master.
'''
from datetime import date
atual = date.today().year

ano = int(input('Qual o seu ano de nascimento·? '))
idade = atual - ano

if idade <= 9:
    print('Mirim')
elif idade <=9:
    print('Infantil')
elif idade <= 25:
    print('Senior')
else:
    print('Master')