print("Bem-vindos à Madeireira do Lenhador Eduardo Sato!")

# Mostra as opções para o cliente escolher qual o tipo de madeira e retorna o respectivo valor.
def escolha_tipo():
    while True:
        print("Escolha o tipo de madeira desejado: ")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        madeira = input(">>")
        if madeira.upper() == "PIN":
            return 150.40
        elif madeira.upper() == "PER":
            return 170.20
        elif madeira.upper() == "MOG":
            return 190.90
        elif madeira.upper() == "IPE":
            return 210.10
        elif madeira.upper() == "IMB":
            return 220.70
        else:
            print("Opção inválida, escolha novamente!\n")
            continue


# Pergunta a quantidade de toras e define as condicionais para dar o respectivo desconto
def qtd_toras():
    while True:
        try:
            toras = int(input("Informe a Quantidade de Toras (m³): "))
            desconto = 0.00
            if toras < 100:
                desconto = 0.00
            elif (toras >= 100) and (toras < 500):
                desconto = 0.04
            elif (toras >= 500) and (toras < 1000):
                desconto = 0.09
            elif (toras >= 1000) and (toras <= 2000):
                desconto = 0.16
            else:
                print("Não aceitamos pedidos com essa quantidade de toras.")
                print("Por favor entre com a quantidade novamente.\n")
                continue
            return toras, desconto
        except:
            print("Digite um valor numérico.\n")
            continue

# Entrada de dados de transporte para ser adicionado posteriormente ao valor total
def transporte():
    while True:
        try:
            print("Escolha o tipo de Transporte: ")
            print("1 - Transporte Rodoviário  - R$ 1000.00")
            print("2 - Transporte Ferroviário - R$ 2000.00")
            print("3 - Transporte Hidroviário - R$ 2500.00")
            transp = int(input(">>"))
            if transp == 1:
                return 1000
            elif transp == 2:
                return 2000
            elif transp == 3:
                return 2500
            else:
                print("Opção inválida, tente novamente.\n")
                continue
        except:
            print("Digite um valor numérico.\n")
            continue

# Programa principal para calcular o valor total do pedido.
tipoMadeira = escolha_tipo()
qtd, desconto = qtd_toras()
frete = transporte()
total = ((tipoMadeira * qtd) * (1 - desconto)) + frete
print(f"Total: R$ {total:.2f}")
