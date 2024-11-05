# Menu com as opções do cardápio.
print("-" * 10, "Bem-vindos à Pizzaria do Eduardo Sato!", "-" * 10)
print("-" * 25, "Cardápio", "-" * 25)
print("-" * 60)
print("-" * 2, "| Tamanho |  Pizza Salgada (PS)  |  Pizza Doce (PD)  |","-" * 2)
print("-" * 2, "|    P    |       R$ 30.00       |     R$ 34.00      |","-" * 2)
print("-" * 2, "|    M    |       R$ 45.00       |     R$ 48.00      |","-" * 2)
print("-" * 2, "|    G    |       R$ 60.00       |     R$ 66.00      |","-" * 2)
print("-" * 60)

# Valor total do pedido
total = 0.00

# Coletando sabor e tamanho escolhidos pelo cliente e validando as respostas com suas respectivas condicionais.
while True:
    sabor = input("\nEscolha o sabor desejado (PS/PD): ")
    if sabor.upper() == "PS":
        tamanho = input("Escolha o tamanho da pizza (P/M/G): ")
        if tamanho.upper() == "P":
            # incremento do preço unitário ao valor total do pedido.
            total += 30
            print("Você pediu uma Pizza Salgada no tamanho P: R$ 30.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        elif tamanho.upper() == "M":
            total += 45
            print("Você pediu uma Pizza Salgada no tamanho M: R$ 45.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        elif tamanho.upper() == "G":
            total += 60
            print("Você pediu uma Pizza Salgada no tamanho G: R$ 60.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        else:
            print("Tamanho inválido. Tente novamente.")
            continue
    elif sabor.upper() == "PD":
        tamanho = input("Escolha o tamanho da pizza (P/M/G): ")
        if tamanho.upper() == "P":
            total += 34
            print("Você pediu uma Pizza Doce no tamanho P: R$ 34.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        elif tamanho.upper() == "M":
            total += 48
            print("Você pediu uma Pizza Doce no tamanho M: R$ 48.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        elif tamanho.upper() == "G":
            total += 66
            print("Você pediu uma Pizza Doce no tamanho G: R$ 66.00\n")
            resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
            if resposta.upper() == "S":
                continue
            elif resposta.upper() == "N":
                print(f"O valor total a ser pago: R$ {total:.2f}")
                break
        else:
            print("Tamanho inválido. Tente novamente.")
            continue
    else:
        print("Sabor inválido. Tente novamente.")
        continue
