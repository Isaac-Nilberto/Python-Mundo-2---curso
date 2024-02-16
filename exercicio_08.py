#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:54:39 2022

@author: isaacnilberto
"""

'''
Questão 8 :
desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso.
- entre 18.5 - 25: peso ideal.
- entre 25 - 30: Sobrepeso.
- entre 30 até 40: obesidade.
- acima de 40: obesidade mórbida.
'''

massa = float(input('Qual sua massa? '))
altura = float(input('Qual sua altura? '))

imc = massa / (altura**2)

if imc < 18.5:
    print(f'Você está abaixo da massa ideal pois seu imc é {imc}')
elif imc >= 18.5 and imc < 25:
    print(f'Você está com a massa ideal pois seu imc é {imc}')
elif imc >= 25 and imc < 30:
    print(f'Você está sobrepeso pois seu imc é {imc}')
elif imc >= 30 and imc < 40:
    print(f'Você está obeso pois seu imc é {imc}')
else:
    print(f'Você está com obesidade mórbida pois seu imc é {imc}')