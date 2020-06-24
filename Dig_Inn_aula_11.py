# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:49:40 2020

@author: Aldo

Aula 11

"""
lista = [1,10,20]
arquivo = open('C:/Users/Aldo/Documents/BACKUP/PycharmProjects/Digital Inovation/teste.txt','r')
try:
    divisão = 10/1
    numero = lista[2]
    x = 1

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero!')    
except ArithmeticError:
    print('Houve um erro ao realizar uma divisão aritmética!')    
except IndexError:
    print('Erro ao acessar um indice fora do intervalo da lista!')

except BaseException as ex:
    print('Erro desconhecido : {}'.format(ex))
else:
    print('O código foi executado com sucesso!')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
    
""" 
É importante saber que os tipos de erros correspondem a uma hierarquia,
essa hierarquia portanto é responsavel por abranger certos tipos de exceções
Para saber a organização da hierarquia é interessante ler a documentação 
disponível no link a seguir: < https://docs.python.org/3/library/exceptions.html > 

    Dada essa consideração é importante devido á lógica iniciar as exeções a partir
das hierarquias mais baixas ou mais específicas, tendo como continuidade as exeções
mais generalistas.
"""

