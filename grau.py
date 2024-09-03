def grau(f):
    return 5 * ((f - 32) / 9)
f=int(input("digite o valor em Fahrenheit:"))
resultado=grau(f)
print(f"O valor em Fahrenheit: {f}°F, valor em Celsius: {resultado:.2f}°C")
