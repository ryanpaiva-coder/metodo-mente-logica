convidados = ["João", "Maria", "Ana"]
for convidado in convidados:
    print(f"{convidado}, te convido para minha festa!")

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]
maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Soma dos números:", soma_numeros)
print("Média dos números:", media_numeros)

frase = input("Digite uma frase: ").lower()
letras = {}
for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1
for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]
numeros_crescente = sorted(numeros)
print("Números em ordem crescente:", numeros_crescente)
numeros_decrescente = sorted(numeros, reverse=True)
print("Números em ordem decrescente:", numeros_decrescente)

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
numero_mes = int(input("Digite um número entre 1 e 12: "))
if 1 <= numero_mes <= 12:
    print(f"O mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 12.")

tarefas = []
while True:
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
        tarefa = input("Digite a tarefa para ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso.")
        else:
            print("Tarefa não encontrada.")
    elif opcao == "3":
        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")