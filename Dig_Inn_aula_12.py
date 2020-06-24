# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 05:37:38 2020

@author: Aldo
"""

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws//{}/json/'.format(cep))
    print(response.status_code)
    #200 significa que houve um sucesso ao realizar a requisição 
    # print(response.text)
    # print(type(response.text))
    print(response.json())
    # print(type(response.json()))
    dados_cep= response.json()
    # print (dados_cep)
    # print(type(dados_cep))
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon
    
def retorna_response(url):
    response=requests.get(url)
    return response.text


if __name__ == '__main__':
    # retorna_dados_cep('01001000')
    # dados_pokemon=retorna_dados_pokemon('charizard')
    # print(retorna_dados_pokemon('charizard'))
    # print(dados_pokemon['sprites'] ['front_shiny'])
    response=retorna_response('https://www.udemy.com/')    
    print(response)
    