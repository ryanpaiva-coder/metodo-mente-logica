frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in frase:
    if letra in vogais:
        contador += 1
print(f"A frase tem {contador} vogais.")

frase = input("Digite uma frase: ")
palavras = frase.split()
frase_invertida = (" ").join(reversed(palavras))
print(f"Frase invertida: {frase_invertida}")

palavra = input("Digite uma palavra: ").lower()
palavra_sem_espaco = palavra.replace(" ", "")
if palavra_sem_espaco == palavra_sem_espaco[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")