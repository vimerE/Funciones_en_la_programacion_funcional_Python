#Ejemplo funciones recursivas

def funcionCuentaRegresiva(numero):
     numero -= 1
     if numero > 0:
         print(numero)
         funcionCuentaRegresiva(numero)
     else:
         print("Explosión")

funcionCuentaRegresiva(5)