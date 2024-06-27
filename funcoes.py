
curso = 'Ensino a Distância'
a = curso.upper()
print(a)
b = curso.lower()
print(b)
c = curso.split()
print(c)

lista_valores = [1, 2, 3, 4, 5]
print(lista_valores)

lista_range = list(range(10))
print(lista_range)

lista_repetida = [0] * 10
print(lista_repetida)

lista_string = list("Olá, mundo!")
print(lista_string)

#Utilizando tuplas
t1 = (1, 2, 3)

t2 = (1,)

t3 = (1, 2, 3)
primeiro_elemento = t3[0]  # Saída: 1

# t = (1, 2, 3)
# t[0] = 4  # Isso resultará em um TypeError

t4 = (1, 2, 3)
a, b, c = t4
# Agora, a é 1, b é 2 e c é 3

print(t1,t2,t3,t4)
