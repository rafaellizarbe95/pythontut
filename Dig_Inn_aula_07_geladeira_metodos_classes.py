class Geladeira:
    def __init__(self):
        self.temperatura= -20
        self.minimo = -2
        self.maximo = 2

    def regularTemperatura(self):
        if self.temperatura > self.maximo:
            self.temperatura -= 1
        elif self.temperatura < self.minimo:
            self.temperatura += 1
        else:
            pass
    
    def mostrarTemperatura (self):
        print('Temperatura atual {} graus Celsius'.format(self.temperatura))

class Torradeira:
    def __init__(self,tempo):
        self.tempo=0
        self.calorAtual=0
        self.calorMaximo=100
    def torrar(self):
        self.tempo += 1
        if self.calorAtual < self.calorMaximo:
            self.calorAtual += 1 + self.calorAtual

class ArCondicionado:

    def __init__(self):
        self.temperatura = 20

    def aumentarTemperatura(self):
        if self.temperatura < 30:
            self.temperatura += 1

    def diminuirTemperatura(self):
        if self.temperatura > 30:
            self.temperatura -= 1

class Calculadora:
    def __init__(self,num1,num2):
        self.valor_1 = num1
        self.valor_2 = num2

    def soma(self):
        return self.valor_1 + self.valor_2
    
    def subt(self):
        return self.valor_1 - self.valor_2
    
    def multiplica(self):
        return self.valor_1 * self.valor_2
    
    def divi(self):
        return self.valor_1 / self.valor_2

if __name__ == '__main__':
    geladeira = Geladeira()
    geladeira.mostrarTemperatura()
    geladeira.regularTemperatura()
    geladeira.mostrarTemperatura()