#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:22:45 2022

@author: isaacnilberto
"""

"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher a base de conversão: 1. binário, 2. octal e 3 hexadecimal.
"""

base_conversao = int(input('Para qual base queres converter o numero: 1. binário, 2. octal ou 3. hexadecimal? '))

numero = int(input('Qual numero queres converter? '))

if base_conversao == 1:
    print(f'O seu numero em binario é: {bin(numero)[2:]}')
elif base_conversao == 2:
    print(f'O seu numero em octal é: {oct(numero)[2:]}')
elif base_conversao == 3:
    print(f'O seu numero em hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção invalida.')