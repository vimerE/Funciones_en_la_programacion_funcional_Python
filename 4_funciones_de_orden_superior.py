#Ejemplo funciones de orden superior

def calcularOperacion(fuerza,m,a,):
	return fuerza(m,a)

def CalcularFuerza(x,y):
	if (x!=0 and y!=0):
		 f = x * y
	else:
		 f = "Valores incorrectos"
	return f

fuerza = calcularOperacion(CalcularFuerza, 11,3)
print('La fuerza es:' , fuerza)





