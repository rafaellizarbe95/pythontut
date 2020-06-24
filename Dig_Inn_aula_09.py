# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:04:52 2020

@author: Aldo

Aula 9 de Python
Manipulação de arquivos 
e mais funções de lambda

Prática:
"""

# arquivo = open ('teste.txt', 'w')
# arquivo.write('Primeira sentença')
# arquivo.close()

# arquivo = open ('teste.txt', 'a')
# arquivo.write('\nSegunda sentença')
# arquivo.close()

# def escrever_arquivo(texto):
#     arquivo = open ('teste.txt','w')
#     arquivo.write (texto)
#     arquivo.close()
    
# def atualizar_arquivo(texto):
#     arquivo = open ('teste.txt','a')
#     arquivo.write (texto)
#     arquivo.close()

# def ler_arquivo(nome_arquivo):
#     arquivo = open (nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)
    
# if __name__ == '__main__':
    # escrever_arquivo('Primeira linha')
    # atualizar_arquivo('\nSegunda linha')
    # ler_arquivo('teste.txt')

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Aldo/PycharmProjects/Digital Inovation/teste.txt'
    arquivo = open (diretorio,'w')
    arquivo.write (texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open (nome_arquivo,'a')
    arquivo.write (texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open (nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
def media_notas (nome_arquivo):
    lista_media =[]
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    for x in aluno_nota:
        lista_notas=x.split(',')
        aluno=lista_notas[0]
        notas=lista_notas[1:]
        print(aluno)
        print(notas)
        # print(len(notas))
        media= lambda nota: sum([int(i) for i in nota])/len(notas)# list comprehension
        print('Média: {}'.format(media(notas)))
        lista_media.append({aluno:media(notas)})
        print(lista_media)
        
def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'C:/Users/Aldo/PycharmProjects/')
def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,'C:/Users/Aldo/PycharmProjects/')
    
        
    

    
if __name__ == '__main__':
    # escrever_arquivo('Primeira linha')
    # atualizar_arquivo('teste.txt','\nSegunda linha')
    # ler_arquivo('teste.txt')
    # texto = 'Jorginho,10,10,5,5\n'
    # atualizar_arquivo('notas.txt', texto)
    media_notas('C:/Users/Aldo/PycharmProjects/Digital Inovation/notas.txt')
    