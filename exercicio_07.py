#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:23:49 2022

@author: isaacnilberto
"""

'''
Questão 7:
Qual tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''

lado_a = float(input('Entre com o lado a: '))
lado_b = float(input('Entre com o lado b: '))
lado_c = float(input('Entre com o lado c: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_b + lado_a:
    print('Os lados dados podem formar um triangulo.')
    if lado_a == lado_b and lado_a == lado_c and lado_b == lado_c:
        print('O triângulo é equilatero.')
    
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('O triângulo é Isósceles.')
    else:
        print('O triângulo é Escaleno')
else:
    print('Não pode formar triangulo')