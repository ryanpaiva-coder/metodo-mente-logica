def divisao():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            dividir = num1 / num2
            return dividir
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero.")
resultado = divisao()
print(f"A divisão é: {resultado}")

def ler_arquivo_usuario():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo não existe.")
    except PermissionError:
        print("Erro: Sem permissão para ler o arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
ler_arquivo_usuario()

def celsius_para_fahrenheit():
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
    except ValueError:
        print("Erro: Por favor, insira um valor numérico.")
    else:
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
celsius_para_fahrenheit()