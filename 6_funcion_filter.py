#Ejemplo funcion Filter

lista_nombres = ['Edem', 'Alisson', 'Jhon', 'Luis', 'Emma','Uriel']
# filter(lambda item: item[] expresion, lista_iterable)
print(list(filter(lambda x: x[0].lower() in 'aeiou', lista_nombres)))