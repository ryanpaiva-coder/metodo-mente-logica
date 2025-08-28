nome = "Ryan"
idade = 21
altura = 1.69
estudante = True

print("Nome: ", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É estudante?", estudante)

ano_nascimento = 2025 - idade
print("Ano de nascimento:", ano_nascimento)

maior_de_idade = idade >= 18
print("É maior de idade?", maior_de_idade)

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos."
print(frase)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("Temperatura em Fahrenheit:", fahrenheit)

raio = float(input("Digite o raio do círculo: "))
pi = 3.14159
area = pi * raio ** 2
print("Área do círculo:", area)