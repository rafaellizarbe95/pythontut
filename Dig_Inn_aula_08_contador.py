# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:34:39 2020

@author: Aldo

Estas anotações vão servir de referencia para o uso de módulos em um script
e também no modo interativo. Classes de outros módulos poderão ser chamadas
a partir de um módulo de cuja localidade é a mesma dos demais.

"""

from Digital_Inovation_07_Televisao import Television
from aula8_modcont import contador_letras,teste

if __name__ == '__main__':
        
    televisao = Television()
    televisao.power()
    televisao.ligada
    lista = ['cachorro','galinha','porco','morcego']
    total_letras=contador_letras(lista)
    print('O total de letras para a lista de animais {} é {} respectivamente'.format(lista,total_letras))
    print(teste())