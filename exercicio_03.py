#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:31:58 2022

@author: isaacnilberto
"""
"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
- o primeiro valor é maior.
- o segundo valor é maior.
- não existe valor maior, os dois são iguais.
"""

primeiro_valor = int(input('Digite o primeiro valor a ser comparado: '))
segundo_valor = int(input('Digite o segundo valor a ser comparado: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior.')
elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')