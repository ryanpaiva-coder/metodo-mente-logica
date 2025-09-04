for i in range(1, 11):
    print(i)

n = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(n + 1):
    soma += i
print("A soma de todos os número de 1 a", n, "é:", soma)

numero_tabuada = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    tabuada = numero_tabuada * i
    print(numero_tabuada, "x", i, "=", tabuada)

par = 0
impar = 0
for i in range(1, 21):
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
print("De 1 a 20 temos", par, "números pares e", impar, "números ímpares.")

import random
numero_secreto = random.randint(1, 100)
tentativas = 0
print("Adivinhe o número entre 1 e 100")    
while True:
    chute = int(input("Faça uma tentativa: "))
    tentativas += 1
    if chute == numero_secreto:
        print("Muito bem! Você acertou em", tentativas, "tentativas.")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

numero = int(input("Digite um número: "))
fatorial = 1
if numero < 0:
    print("Não existe fatorial de número negativo.")
elif numero == 0 or numero == 1:
    print(f"O fatorial de {numero} é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")

quantia_casas = int(input("Digite quantos termos da série Fibonacci você quer ver: "))
termo1 = 0
termo2 = 1
contador = 0
if quantia_casas <= 0:
    print("Por favor, insira um número positivo.")
elif quantia_casas == 1:
    print("Série Fibonacci até", quantia_casas, "termo:")
    print(termo1)
else:
    print("Série Fibonacci:")
    while contador < quantia_casas:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1