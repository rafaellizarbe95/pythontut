# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:54:21 2020

@author: Aldo

Mini projeto da Aula 11, vamos colocar os tratamentos de exeções em prática
Para isso foi adaptada um outro exercício, de cujo algoritmo busca encontrar os 
zeros (raízes) de uma equação quadrática de segundo grau.

"""

import math

class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message

resposta = input('Você irá resolver uma equação de segundo grau, para isso é necessário passar algumas informaões, deseja continuar? [S/N]')

if resposta == ('S') or resposta == ('s'):
    
    while True: 
        
        try:
            a=float(input('Considerando a equação : a(x^2)+bx+c, digite "a":'))
            b=float(input('Considerando a equação : a(x^2)+bx+c, digite "b":'))
            c=float(input('Considerando a equação : a(x^2)+bx+c, digite "c":'))
            delta=(b**2)-(4*a*c)
            
            if delta <=0:
                raise InputError('Não é possível resolver esta equação, o delta não pode ser negativo!')
            break
        
        except ValueError:
            print('Digite apenas números inteiros por favor')
            
        finally:
            raizdelta = math.sqrt(delta)
            x1=(-b + raizdelta )/(2*a)
            x2=(-b - raizdelta )/(2*a)
            print('As raízes da equação quadrática são x1= {} e x2= {}'.format(x1,x2))

else:
    exit
    