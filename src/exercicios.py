

lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4]

test = [result[0] + result[0] for result in list(zip(lista_a, lista_b))]
print(test)
