
lista = [1, 10]
try:
    divisao =  10 / 1
    numero = lista[3]
    x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido na lista.')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))