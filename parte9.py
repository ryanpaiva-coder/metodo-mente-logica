import conversoes

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade atual (C, F, K): ").upper()
converter_para = input("Converter para (C, F, K): ").upper()
if unidade == "C":
    if converter_para == "F":
        resultado = conversoes.celsius_para_fahrenheit(temperatura)
    elif converter_para == "K":
        resultado = conversoes.celsius_para_kelvin(temperatura)
elif unidade == "F":
    if converter_para == "C":
        resultado = conversoes.fahrenheit_para_celsius(temperatura)
    elif converter_para == "K":
        celsius = conversoes.fahrenheit_para_celsius(temperatura)
        resultado = conversoes.celsius_para_kelvin(celsius)
elif unidade == "K":
    if converter_para == "C":
        resultado = conversoes.kelvin_para_celsius(temperatura)
    elif converter_para == "F":
        celsius = conversoes.kelvin_para_celsius(temperatura)
        resultado = conversoes.celsius_para_fahrenheit(celsius)
else:
    resultado = "Unidade inválida."
print(f"Temperatura convertida: {resultado} {converter_para}.")