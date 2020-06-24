# Detalhes do que será desenvolvido neste tópico
# O que é um conjunto 
# Método de união 
# Método de Intersecção
# Método de diferença
# Método de diferença simétrica
# Remoção de duplicidade de listas usando conjuntos


# Em conjuntos se utilizam chaves '{}' designado como set com o comando 'type' 

# conjunto = {1,2,3,4,5,6}
# print(type(conjunto))

# conjunto.add(3)
# conjunto.discard(3)

# conjunto = {1,2,3,4,5}
# conjunto2 = {5,6,7,8}
# conjuntouniao = conjunto.union(conjunto2)
# print(conjuntouniao)

# conjuntintersect = conjunto.intersection(conjunto2)
# print(conjuntintersect)

# conjuntodiferen = conjunto.difference(conjunto2)
# print(conjuntodiferen)
# conjuntodif2 = conjunto2.difference(conjunto)
# print(conjuntodif2)

# print('União : {}'.format(conjuntouniao))
# print('Intersecção : {}'.format(conjuntintersect))

# diferencasim = conjunto.symmetric_difference(conjunto2)
# print(diferencasim)
# conj1 = {1,2,3,4,5,6,7,8,9}
# conjin = {2,4,6}
# conjusubset = conjin.issubset(conj1)
# print(conjusubset)
# conjusuper = conjin.issuperset(conj1)
# print(conjusuper)

# # conjuntos podem também ser transformados em listas
# lista=list(conj1)
# print(lista)
# # Listas também podem ser convertidas em conjuntos
# conjuntolista=set(lista)
# print(conjuntolista)

conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}
conjun = conjunto1.union(conjunto2)
print(conjun)
