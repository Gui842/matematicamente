import math
def teorema(catetoA,catetob):
    return math.sqrt(catetoA**2+catetob**2)
catetoA=int(input("digite o valor do catetoto A:"))
catetob=int(input("digite o valor do cateto B:"))
hipotenusa=teorema(catetoA,catetob)
print(" o valor da hipotenusa é",hipotenusa)