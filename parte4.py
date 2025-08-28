numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 60:
    print("Você é um idoso.")
else:
    print("Idade inválida.")

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

valor_saque = int(input("Digite o valor do saque: R$"))
if valor_saque <= 0:
    print("Valor inválido.")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    cedulas_2 = valor_saque // 2
    valor_saque %= 2
    if valor_saque != 0:
        print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
    else:
        print("Cédulas entregues:")
        if cedulas_100 > 0:
            print(f"{cedulas_100} x R$100")
        if cedulas_50 > 0:
            print(f"{cedulas_50} x R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} x R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} x R$10")
        if cedulas_5 > 0:
            print(f"{cedulas_5} x R$5")
        if cedulas_2 > 0:
            print(f"{cedulas_2} x R$2")

valor_emprestimo = float(input("Digite o valor do empréstimo: R$"))
renda_mensal = float(input("Digite sua renda mensal: R$"))
numero_parcelas = int(input("Digite o número de parcelas: "))
valor_parcela = valor_emprestimo / numero_parcelas
limite_parcela = renda_mensal * 0.30
if valor_parcela <= limite_parcela:
    print("Empréstimo aprovado.")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
else:
    print("Empréstimo negado.")
    print(f"Valor da parcela R${valor_parcela:.2f} excede 30% da renda mensal.")

import random
opcoes = ["pedra", "papel", "tesoura"]
usuario = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)
print(f"Você escolheu: {usuario}")
print(f"O computador escolheu: {computador}")
if usuario == computador:
    print("Empate!")
elif (usuario == "pedra" and computador == "tesoura") or (usuario == "papel" and computador == "pedra") or (usuario == "tesoura" and computador == "papel"):
    print("Você venceu!")
elif usuario in opcoes:
    print("Você perdeu!")
else:
    print("Escolha inválida.")

distancia = float(input("Digite a distância percorrida em km: "))
tarifa_basica = 4.00
custo_por_km = 0.25
valor_total = tarifa_basica + (custo_por_km * distancia)
print(f"Valor total da corrida: R${valor_total:.2f}")