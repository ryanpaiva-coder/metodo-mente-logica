agenda = {}
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")
def buscar_contato():
    nome = input("Nome do contato a buscar: ")
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")
def remover_contato():
    nome = input("Nome do contato a remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")
while True:
    print("\nAgenda Telefônica:")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

frase = input("Digite uma frase: ")
palavras = frase.split()
palavras_unicas = set(palavras)
print("Palavras únicas:", palavras_unicas)

entrada_a = input("Digite uma sequência de números separados por espaço: ").split()
entrada_b = input("Digite uma sequência de números separados por espaço: ").split()
numeros_a = set(entrada_a)
numeros_b = set(entrada_b)
uniao = numeros_a.union(numeros_b)
intersecao = numeros_a.intersection(numeros_a)
print("União dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)

texto = input("Digite um texto: ")
contagem = {}
for caractere in texto:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1
print("Contagem de caracteres:")
for caractere, quantidade in contagem.items():
    print(f"'{caractere}': {quantidade}")