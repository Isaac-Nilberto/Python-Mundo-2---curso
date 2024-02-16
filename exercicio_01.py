#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:08:29 2022

@author: isaacnilberto
"""

"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado.
"""
#%% minha solucao
valor_casa = float(input('Qual valor da casa que tu queres comprar? '))

salario_comprador = float(input('Por questões da empresa, qual seu o salário? '))

anos_pagamento = int(input('Em quantos anos tu vais pagar? ')) * 12

print('O total de meses é {}'.format(anos_pagamento))

prestacao = valor_casa/anos_pagamento
print('O valor mensal da sua prestação sem juros é de {}'.format(prestacao))
if prestacao > salario_comprador * 0.3:
    print('Você não pode ter acesso ao emprestimo.')
else:
    print('Você tem acesso ao emprestimo.')

