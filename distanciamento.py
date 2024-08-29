import math
def distanciamento(So,S):
     return S-So
S=int(input("digite o valor final:"))
So=int(input("digite o valor inicial:"))
resultado=distanciamento(S,So)
if resultado >=0:
    print(f"{resultado}(M/KM): esta indo")
else:
    print( resultado,"(M/KM): esta voltando"
