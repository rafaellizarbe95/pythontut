# É interessante observar que serão aprendidos alguns comandos em especial
# são estes if elif e else, são essenciais para o condicionamento de determinadas
# funções em determinados tipos de trabalho
# Neste caso temos uma operação simples de interação, ou seja serão introduzidos valores e de acordo com
# os nùmeros colocados. A seguir serão dadas respostas adequadas ao condicionamento maior ou menor:
import os
os.system('cls') or None
# a = int(input("Primeiro número: "))
# b = int(input("Segundo número: "))
# if a > b:
#     print("{} é maior que {}!".format(a, b))
# elif b > a:
#     print(" {} é menor que {}!".format(a, b))
# else:
#     print(" Os números digitados são iguais!")
# print("Final do programa")

# A seguir temos outro programa que segue o exemplo da aula, neste o programa mostra qual dos nùmeros computados
# seráo designados como maiores para o comando print

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print(' O maior número é {}'.format(c))
print('final do programa')

#  Ele também mostra um exemplo de programa no qual é possível definir se o número é par ou impar

# a = int(input('Digite um número: '))
# b = int(input('Digite um número: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b ==0:
#     print('Pelo menos um número par foi digitado')
# else:
#     print('Nenhum número par foi digitado!')

# na linha 38 é possível perceber que há um parametro 'or', a este se pode acrecentar o parametro 'not' o qual
# será bastante util para designar o oposto do que está escrito no programa além de or também poderá ser utilizado
# o acrecentador 'and'.
# a = int(input("Digite a nota do Primeiro Bimestre:"))
# b = int(input("Digite a nota do Segundo Bimestre:"))
# c = int(input("Digite a nota do Terceiro Bimestre:"))
# d = int(input("Digite a nota do Quarto Bimestre:"))
# media_peso1=(a+b+c+d)/4
# print('A média aritmética simples de suas notas é {}'.format(media_peso1))
# #
# a = int(input("Digite a nota do Primeiro Bimestre:"))
# b = int(input("Digite a nota do Segundo Bimestre:"))
# c = int(input("Digite a nota do Terceiro Bimestre:"))
# d = int(input("Digite a nota do Quarto Bimestre:"))
# media_peso1=(a+b+c+d)/4
# if a<=10 and b<=10 and c<=10 and d<=10:
#     print('A média aritmética simples de suas notas é {}'.format(media_peso1))
# else:
#     print('Você digitou algum valor errado, coloque apenas valores menores ou iguais a 10!')
#
a = int(input("Digite a nota do Primeiro Bimestre:"))
if a>10:
    a = int(input('Você devará colocar valores menores ou iguais a 10! Digite a nota do Primeiro Bimestre:'))
b = int(input("Digite a nota do Segundo Bimestre:"))
if b>10:
    b = int(input('Você devará colocar valores menores ou iguais a 10! Digite a nota do Segundo Bimestre:'))
c = int(input("Digite a nota do Terceiro Bimestre:"))
if c>10:
    c = int(input('Você devará colocar valores menores ou iguais a 10! Digite a nota do Terceiro Bimestre:'))
d = int(input("Digite a nota do Quarto Bimestre:"))
if d>10:
    d = int(input('Você devará colocar valores menores ou iguais a 10! Digite a nota do Quarto Bimestre:'))
media_peso1=(a+b+c+d)/4
if a<=10 and b<=10 and c<=10 and d<=10:
    print('A média aritmética simples de suas notas é {}'.format(media_peso1))
else:
    print('Você digitou algum valor errado, coloque apenas valores menores ou iguais a 10!')

#Aula encerrada!!!

#Questão de prova,

# a = 10
# b = 10
# c = 10
# if a > b or a >= c:
#     print('Primeiro afirmação é verdadeira')
# elif a == b:
#     print('Segunda afirmação é verdadeira')
# else:
#     print('Nenhuma afirmação é verdadeira')

