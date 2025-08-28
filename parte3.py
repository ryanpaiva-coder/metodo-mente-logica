pao = 3.50
leite = 4.20
cafe = 2.80
total_compra = pao + leite + cafe
valor_pago = 20.00
troco = valor_pago - total_compra
print("Total da compra é: R$", total_compra)
print("O troco é: R$", troco)

nota_media = 8.5
frequencia = 80
nota_minima = 7.0
frequencia_minima = 75
aprovado = (nota_media >= nota_minima) and (frequencia >= frequencia_minima)
print("O aluno está aprovado?", aprovado)

quantidade_itens = 8
total_compra = 120.00
desconto = (quantidade_itens > 10) or (total_compra > 100)
print("O cliente tem direito ao desconto?", desconto)

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False
acesso = (senha_inserida == senha_correta) and not usuario_bloqueado
print("O acesso foi concedido?", acesso)

conta = 150.00
amigos = 3
valor_por_amigo = conta / amigos
valor_exato = (conta % amigos) == 0
print("Cada amigo deve pagar: R$", valor_por_amigo)
print("O valor é exato para divisão entre amigos?", valor_exato)

idade = int(input("Digite sua idade: "))
pode_ver_filme = idade >= 16
print("Você pode ver o filme?", pode_ver_filme)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
peso_ideal = (imc >= 18.5) and (imc <= 24.9)
print("Seu IMC é:", imc)
print("Você está com peso ideal?", peso_ideal)

numero = int(input("Digite um número inteiro: "))
par = (numero % 2) == 0
print("O número é par?", par)