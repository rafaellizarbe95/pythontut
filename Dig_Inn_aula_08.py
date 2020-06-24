# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:24:15 2020

@author: Aldo

Funções lambda funções anônimas...
"""
lista_animais = ['cachorro','elefante','gato']

contador_letras = lambda lista: [len(x) for x in lista ]

print(contador_letras(lista_animais))

soma = lambda a,b : a + b
subt = lambda a,b : a-b

print(soma(5,10))
print(subt(10,5))

calculadora = {
    'sum': lambda a, b : a + b,
    'subt': lambda a , b : a - b,
    'mult': lambda a,b : a * b,
    'div': lambda a,b : a / b
    }
soma = calculadora['sum']
subt = calculadora['subt']
mult = calculadora['mult']
div = calculadora ['div']

print(soma(2,3))

