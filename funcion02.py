import math

def raiz(n):
    return math.sqrt(n)
def potencia(n):
    return math.pow(n,5)
def logaritmo(n):
    return math.log10(n)

x = int(input("N:"))
print("La raiz cuadradra: ", raiz(x))
print("La potencia: ", potencia(x))
print("El logaritmo: ", logaritmo(x))

