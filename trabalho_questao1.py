print("Sistema desenvolvido por Eduardo Sato")

# Coletando os dados de valor base e idade do cliente.
valorBase = float(input("Informe o Valor Base do plano: R$ "))
idade = int(input("Informe a Idade do cliente: "))

# Verificação da idade do cliente para calcular valor final do plano.
if (idade >= 0) and (idade < 19):
    valorMensal = valorBase * 1
elif (idade >= 19) and (idade < 29):
    valorMensal = valorBase * 1.5
elif (idade >= 29) and (idade < 39):
    valorMensal = valorBase * 2.25
elif (idade >= 39) and (idade < 49):
    valorMensal = valorBase * 2.4
elif (idade >= 49) and (idade < 59):
    valorMensal = valorBase * 3.5
else:
    valorMensal = valorBase * 6

# Saída final na tela informando o valor mensal do plano.
print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")
