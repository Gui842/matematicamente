def soma(valor1,valor2): 
      return valor1+valor2 
def divisao(valor1,valor2):
    return valor1/valor2
def subtracao(valor1,valor2):
    return valor1-valor2
def mutiplicacao(valor1,valor2):
    return valor1*valor2

valor1=int(input("digite um numero:"))
valor2=int(input("digite um outro numero:"))
operacao=int(input("escolha 1:para divisão,2: para subtração,3: para subtração e 4: para mutiplicação:"))


if operacao ==1:
 resultado=soma(valor1,valor2)
 print(resultado,"resultado")

elif operacao==2:
    resultado=divisao(valor1,valor2)
    print(resultado,"resultado")
elif operacao==3:
    resultado=subtracao(valor1,valor2)
    print(resultado,"resultado")
elif operacao==4:
    resultado=mutiplicacao(valor1,valor2)
    print(resultado,"resultado")
else:
    print("operação invalida!")