import math  

def area_triangulo(b,h):
    return b*h/2
 
def area_quadrado(l):
    return l**2
def area_losango(D,d):
    return D*d/2
def area_retangulo(b,h):
    return b*h
def area_trapezio(B,b,h):
    return (b+b)*h/2

def area_circulo(r):
    return math.pi*r**2

area=int(input("digite 1 para calcular área de um triangulo ,2:para calcular área de um quadrado,3: área de um losango 4:área de um retangulo,5: área de um trapezio,6:área de um circulo:"))

if area==1:
    b=int(input("digite o valor da base:"))
    h=int(input("digite o valor da altura:"))
    resposta=area_triangulo(b,h)
    print( " o valor da base é",b,"o valor da altura é:",h,"por tanto a resposta é",resposta)
elif area==2:
    l=int(input("digite o valor de um lado: "))
    resposta=area_quadrado(l)
    print(" o valor de um lado é" , l,"por tanto a resposta é",resposta)
elif area==3:
    D=int(input("digite o valor da dialonal maior:"))
    d=int(input("digite o valor da dialonal meno:"))
    resposta=area_losango(D,d)
    print("o valor da diagonal maior é:",D , " e da diogonal meno é ",d,"por tanto a resposta é:", resposta)
elif area ==3:
    h=int(input("digite o valor da altura:"))
    b=int(input("digite o valor da base:"))
    resposta=area_retangulo(b,h)
    print( "valor da base é" ,b," o valor da altura é" ,h,"por tanto a resposta é:",resposta)
elif area ==4:
    b=int(input(" digite o valor da base"))
    h=int(input("digite o valor da altura"))
    resposta=area_trapezio(b,h)
    print(" o valor da base é:",b," o valor da altura é:","por tanto a resposta é:", resposta)
elif area==5:
    r=int(input("digite o valor do raio:"))
    resposta=area_circulo(r)
    print( " o valor de pi aproximadamente e de 3,14", " o valor do raio é:",r," por tanto a resposta é:", resposta)
else:
    print("área invalida")