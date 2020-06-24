# Construindo Métodos, Funções e classes com Python


# Aprender a utilização de métodos em Python

# Aprender a utilização de classes

# Entender os motivos para se usar métodos, funções e classes
# O que são métodos e funções
# Como declarar métodos e funções 
# Vantagens de se utilizar métodos e funções
# Como implementar class;
# Vantagem de se utilizar classes


# def soma (a, b):
#     return a + b

# def sub (a, b):
#     return a - b

# def div(a,b):
#     return a / b

# def mult(a,b):
#     return a * b

# print (soma (3,5))
# print (sub (2,2))
# print (div (2,3))
# print (mult(2,5))

# Classes

class Calculadora:
    # def __init__(self,num1,num2):
    #     pass
    def soma (self,valor_a,valor_b):
        return valor_a + valor_b

    def sub (self,valor_a,valor_b):
        return valor_a - valor_b

    def div(self,valor_a,valor_b):
        return valor_a / valor_b

    def mult(self,valor_a,valor_b):
        return valor_a * valor_b

calculadora=Calculadora()
