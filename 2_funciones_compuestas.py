#Ejemplo funciones compuestas

def funcionCalcular(funcion,n):
	return funcion(funcion(n))

def funcionSumar(a):
	return a+a

print (funcionCalcular(funcionSumar,3))




