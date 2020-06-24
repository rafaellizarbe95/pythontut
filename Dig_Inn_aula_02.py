a = 34
b = 26
c = 23
print( "Temos três números {}, {} e {}, estes foram multiplicados e somados,". format (a,b,c) + " o número {a} foi dívidido por {b}.".format(a=a,b=b))
soma = a + b +c
mult = a * b * c
div = a / b
print("     Multiplicação: " + str(mult ))
print("     Soma: " + str(soma))
print("     Divisão de {a} por{b}:".format(a=a,b=b)+ str(div))
