#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:39:32 2022

@author: isaacnilberto
"""
 
lista_pessoas = []
for i in range(0,2):
    nome = input("Qual nome: ")
    idade = float(input("Qual idade: "))
    sexo = input("qual sexo? escreva H ou M: ")
    lista_pessoas.append({"nome: ": nome,"idade: ": idade,"sexo: ": sexo})
print(lista_pessoas)


#%%%%
import pandas as pd
f = 0
for i in lista_pessoas:
   f = i["idade: "]
   f1 += f
print(f1)