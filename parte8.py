def somar(a, b):
    resultado = a + b
    return resultado
def subtrair(a, b):
    resultado = a - b
    return resultado
def multiplicar(a, b):
    resultado = a * b
    return resultado
def dividir(a, b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        print("Erro: Divisão por zero!")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
if operacao == "+":
    print("Adição:", somar(numero1, numero2))
elif operacao == "-":
    print("Subtração:", subtrair(numero1, numero2))
elif operacao == "*":
    print("Multiplicação:", multiplicar(numero1, numero2))
elif operacao == "/":
    print("Divisão:", dividir(numero1, numero2))
else:
    print("Operação inválida!")

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
num = int(input("Digite um número inteiro: "))
if eh_primo(num):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9
def celsius_para_kelvin(c):
    return c + 273.15
def kelvin_para_celsius(k):
    return k - 273.15
temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade atual (C, F, K): ").upper()
converter_para = input("Converter para (C, F, K): ").upper()
if unidade == "C":
    if converter_para == "F":
        resultado = celsius_para_fahrenheit(temperatura)
    elif converter_para == "K":
        resultado = celsius_para_kelvin(temperatura)
elif unidade == "F":
    if converter_para == "C":
        resultado = fahrenheit_para_celsius(temperatura)
    elif converter_para == "K":
        celsius = fahrenheit_para_celsius(temperatura)
        resultado = celsius_para_kelvin(celsius)
elif unidade == "K":
    if converter_para == "C":
        resultado = kelvin_para_celsius(temperatura)
    elif converter_para == "F":
        celsius = kelvin_para_celsius(temperatura)
        resultado = celsius_para_fahrenheit(celsius)
else:
    resultado = "Unidade inválida."
print(f"Temperatura convertida: {resultado} {converter_para}.")