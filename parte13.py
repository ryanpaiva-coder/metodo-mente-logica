nome_arquivo = input("Digite o nome de arquivo: ")
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    palavras = conteudo.lower().split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.strip('.,!?";:-()')
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")

import csv
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    with open('contatos.csv', 'a', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, telefone, email])
    print("Contato adicionado com sucesso.")
def listar_contatos():
    try:
        with open('contatos.csv', 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(f"Nome: {linha[0]}, Telefone: {linha[1]}, Email: {linha[2]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")
while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")

import json
try:
    with open('produtos.json', 'r') as arquivo:
        produtos = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print("-" * 20)

origem = input("Digite o nome do arquivo de origem: ")
destino = input("Digite o nome do arquivo de destino: ")
try:
    with open(origem, 'rb') as arquivo_origem:
        conteudo = arquivo_origem.read()
    with open(destino, 'wb') as arquivo_destino:
        arquivo_destino.write(conteudo)
except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
else:
    print(f"Arquivo {destino} criado com sucesso.")