import math
def temperatura(celsius):
    return celsius* 9/5 + 32
celsius=int(input("digite o valor em  grau celsius:"))
resultado=temperatura(celsius)
print( resultado, "Fahrenheit")