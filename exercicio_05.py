#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:58:39 2022

@author: isaacnilberto
"""

"""
Escreva um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado.
- média de 5.0-6.9: recuperação.
- média 7 ou superior: aprovado.
"""

primeira_avaliacao = float(input('Qual a sua nota da primeira avaliacao: '))

segunda_avaliacao = float(input('Qual a sua nota da primeira avaliacao: '))

media = (primeira_avaliacao + segunda_avaliacao) / 2

if media < 5:
    print(f'Você está reprovado {media}.')
    
elif media >= 5 and media <= 6.9:
    print(f'Você está de recuperacao {media}.')
else:
    print(f'Você esta aprovado {media}.')