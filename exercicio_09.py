#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:03:49 2022

@author: isaacnilberto
"""
'''
Questão 9:
Escreva um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''

valor_produto = float(input('Qual o valor do produto? '))

tipo_pagamento = int(input('Qual tipo de pagamento?\n 1. à vista dinheiro ou cheque 10% de desconto \n 2. à vista cartão 5% de desconto\n 3. parcelado de 2x preço normal \n 4. 3x ou mais no cartão: 20% de juros \n digite: '))
if tipo_pagamento == 1:
    desconto = valor_produto - (valor_produto * 0.1)
    print(f'Seu valor a ser pago com 10% de desconto é {desconto}')
elif tipo_pagamento == 2:
    desconto = valor_produto - (valor_produto * 0.05)
    print(f'Seu valor a ser pago com 10% de desconto é {desconto}')
elif tipo_pagamento == 3:
    parcela = valor_produto / 2
    print(f'Seu valor a ser pago é {valor_produto} e a parcela será de {parcela}')
else:
    totalparc = int(input('Quantas parcelas?'))
    sem_desconto = valor_produto + (valor_produto * 0.2)
    print(f'Seu valor a ser pago com juros de 20% é {sem_desconto} em {totalparc} vezes')