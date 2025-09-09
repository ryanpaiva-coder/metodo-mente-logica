import random

pontuacoes = []

print("Bem-vindo ao Jogo de Adivinhação!")

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 7
    tentativas = 0

    print("\nAdivinhe o número entre 1 e 100.")

    while tentativas_restantes > 0:
        palpite = input("\nDigite seu palpite: ")

        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            pontuacao = tentativas_restantes * 10
            pontuacoes.append(pontuacao)
            print(f"Parabéns, você acertou! O número secreto era {numero_secreto} em {tentativas} tentativas.")
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")
    else:
        print(f"\nSuas tentativas acabaram, o número secreto era {numero_secreto}.")
        pontuacoes.append(0)

    print("\nPlacar:")
    for idx, pontos in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pontos} pontos")
    
    jogar_novamente = input("\nQuer jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar! Até a próxima.")
        break