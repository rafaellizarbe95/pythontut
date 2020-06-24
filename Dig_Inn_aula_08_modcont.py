# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:00:16 2020

@author: Aldo
"""


def contador_letras(lista_palavras):
    contador =[]
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
def teste():
    return 'teste'
    
if __name__ == '__main__':
    lista = ['cachorro','galinha','porco','morcego']
    print(contador_letras(lista))
    
    

        