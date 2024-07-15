import math
def calcular_delta(b,a,c):
    return b**2-4*a*c 
def  baskara(x,a,b):
    return  -b+math.sqrt(x)/2*a

def calcular_as_raizes(a,b,c):
 return -b+math.sqrt(b**2-4*a*c)/2*a

operacao=int(input("escolha oque vocé quer calcular 1: valor de delta, 2:valorr de x , 3 para calcular as raizes:"))
if operacao==1:
    b=int(input("qual é o valor de b:"))
    a=int(input("qual é o valor de a:"))
    c=int(input("qual é o valor de c:"))
    resposta=calcular_delta(b,a,c)
    print("resposta:", resposta)
    
elif operacao ==2:
    b=int(input("qual é o valor de b:"))
    a=int(input("qual é o valor de a:"))
    x=int(input("qual é o valor de delta:"))
    resposta=baskara(a,b,x)
    print(" a resposta de x é:",resposta)

    print("o valor de x é:", "+",resposta,"ou","-",resposta)
elif operacao ==3:
    a=int(input("digite o valor de a:"))
    b=int(input("digite o valor de b:"))
    c=int(input("digite o valor de c:"))
    resposta=calcular_as_raizes(a,b,c)
    print("as raizes são:","+" ,resposta, "-" ,resposta)
    
else:
    print("operação invalida!")