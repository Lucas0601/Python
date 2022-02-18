# 1.Aprender sobre listas
# 2.Aprender sobre tuplas
# 3.Aplicabilidade de listas e tuplas

# Como criar uma lista, Manipular listas, Realizar operações com listas
# O que é são tuplas? Como interagir com tuplas, Conversões de listas e tuplas

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)








# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#      print('não existe um cachorro na lista. Será incluído.')
#      lista_animal.append('lobo')
#      print(lista_animal)
#
#      lista_animal.pop()
#      print(lista_animal)

# Multiplicando a lista
# nova_lista = lista_animal * 3
# print(nova_lista)

# print(lista_animal[1])

# print (sum(lista))
# print (min(lista))
# print (max(lista))

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)