# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:56:18 2020

@author: Aldo

Aula 10 faltam 2as

Trabalhando com dados que envolvem DATE

"""

from datetime import date, time, datetime # importando classes 'date' e 'time' do módulo 'datetime'
""" datetime é um módulo presente nos arquivos do Python3, é possível analisar
o código fonte e trabalhar em cima dele caso haja a necessidade de traduzir , 
é recomendável, logicamente criar outro módulo e traduzir o anterior a partir daí..."""
data_atual = date.today()
# print (data_atual)
def trabalhando_com_date():
    print (data_atual.strftime('%d/%m/%Y'))
    """strftime irá converter para string o formato que irá ser informado diretivas
      do python através de diretivas do python, para mais informações consultar o 
      link a seguir : < https://docs.python.org/3/library/datetime.html >"""
    data_atual_str=data_atual.strftime('%A-%B-%Y') 
    print(type(data_atual)) 
    print(data_atual_str)
    print(type(data_atual_str))
def trabalhando_com_time():
    horario=time(hour = 12, minute =34, second=55)
    print(type(horario))
    print(horario.strftime('%H:%M:%S'))
    horario = horario.strftime('%H:%M:%S')
    print(type(horario))
def trabalhando_com_date_time():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo')
    print(tupla[data_atual.weekday()])
    pass


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_date_time()
    
# passei o modulo