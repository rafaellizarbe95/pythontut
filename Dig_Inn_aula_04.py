
# a = 100
# range (1, a-5)

import os 
os.system('cls') or None

 ### INÍCIO DA AULA PRATICAMENTE ###
# for x in range (100):
#     print (x)

### COMANDO 'for' ###

# for x in range (1,101):
#     print (x)

# for x in range (90,101):
#     print(x)


#### este número é primo??  ###


# a = int(input('Digite um número: '))
# div=0
# for x in range (1, a+1):
#     resto = a % x
#     if resto ==0:
#         div = div +1
# if div == 2:
#     print('O número digitado é primo')
# else:
#     print('O número diitado não é primo')

####    Plataforma PC   ####
####    Programa para   ####
####    Mostrar os n    ####
####    primos <= que   ####
####    o input         ####

# isprime=int(input("Este programa serve para mostrar os números primos menores ou iguais ao número escolhido, digite um número! :"))
# div = 0
# for a in range (isprime+1):
#     div=0
#     for x in range (1,a+1):
#         resto = a % x
#         if resto == 0:
#             div +=1
#     if div == 2:
#         print(x)
#     else:
#       div = 0

# div = 0
# a = int(input('número porra'))
# for x in range (1, a+1):
#     resto = a % x
#     if resto == 0: # se o resto da divisão de a por x for igual a 0 realize a seguinte função:
#         div = div+1
#         # div += 1
#         # a função acima somará também
# if div == 2 :
#     print('O número {} é Primo!'.format(a))
# else:
#     print('O número {} não é Primo!'. format(a))



# a = int(input('Digite um número para computar:'))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     if resto == 0:
#         div = div +1
#
# if div == 2 :
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo.'.format(a))
#.
####                                ####
####    PRIMO,  PAR OU  IMPAR   ?   ####
####                                ####

a = int(input('Digite um número porra!'))
div=0
for x in range (1,a+1):
    resto = a % x
    if resto == 0:
        div = div+1
if div ==2 :
    print('Este número que você digitou é primo doidão!')
else:
    diferenca = a % 2
    if diferenca == 0:
        print("Este número que você digitou é par maluco!")
    else:
        print('Este número que você digitou é impar maluco!')

####    Celular     ####
####    Redmi 5     ####
####    Qpython     ####


# a= int(input('Escreva um número por gentileza:'))
# div = 0
# for x in range (1,a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
# if div == 2:
#      print('O número digitado é Primo!')
# else:
#     diferenca = a % 2
#     if diferenca == 0:
#         print('O numero digitado é Par!')
#     else:
#         print('O número digitado é Impar!')


# a= int(input('Escreva um número por gentileza:'))
# div = 0
# for x in range(1, a+1):
#    	resto = a % x
#    	if resto == 0:
#         div = div + 1
# if div == 2:
#      print('O número digitado é Primo!')
# else:
#     diferenca = a % 2
#     if diferenca == 0:
#         print('O numero digitado é Par!')
#     else:
#         print('O número digitado é Impar!')