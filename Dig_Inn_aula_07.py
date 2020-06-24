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
    def __init__(self,num1,num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma (self):
        return self.valor_a + self.valor_b

    def sub (self):
        return self.valor_a - self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

calculadora=Calculadora(12,45)
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.div())


