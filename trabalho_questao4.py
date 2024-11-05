print("Bem-vindos a lista de contatos do Eduardo Sato!")

lista_contatos = []
id_global = 4955563


# Cadastrar novos contatos a partir de uma função que fará a captação dos dados de entrada.
def cadastrar_contato(id):
    print("-" * 40)
    print("-" * 8, "MENU CADASTRAR CONTATO", "-" * 8)
    nome = input("Inserir o nome do contato: ")
    atividade = input("Inserir a atividade do contato: ")
    telefone = input("Inserir o telefone do contato: ")
    # uso de dicionário para salvar informações de cada pessoa
    contatos = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }
    # copia os dados do dicionário para dentro da lista de contatos
    lista_contatos.append(contatos.copy())


# Menu de consulta para encontrar todos os contatos, ou buscar por id e atividade.
def consultar_contato():
    while True:
        print("-" * 40)
        print("-" * 7, "MENU CONSULTAR CONTATOS", "-" * 7)
        print("1 - Consultar Todos")
        print("2 - Consultar ID")
        print("3 - Consultar Atividade")
        print("4 - Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))
        # Condicionais para realização da busca por segmento: todos, id ou atividade.
        if opcao == 1:
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    print(f"{chave}: {valor}")
                print("\n")
        elif opcao == 2:
            id_consulta = int(input("Digite o ID do contato: "))
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    if contato["id"] == id_consulta:
                        print(f"{chave}: {valor}")
                print("\n")
        elif opcao == 3:
            atividade_consulta = input("Digite a atividade do contato: ")
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    if contato["atividade"] == atividade_consulta.lower():
                        print(f"{chave}: {valor}")
                print("\n")
        elif opcao == 4:
            break
        else:
            print("Opção inválida")
            continue


# função para remover contato da lista através do ID informado.
def remover_contato():
    print("-" * 40)
    print("-" * 8, "MENU REMOVER CONTATO", "-" * 8)
    id_contato = int(input("Informe o ID para remover contato: "))
    for contato in lista_contatos:
        if  id_contato == contato["id"]:
            lista_contatos.remove(contato)
            print("Contato removido!")
        else:
            print("ID Inválido.")


# programa principal com menu e estrutura de repetição.
while True:
    print("-" * 40)
    print("-" * 12, "MENU PRINCIPAL", "-" * 12)
    print("1 - CADASTRAR CONTATO")
    print("2 - CONSULTAR CONTATO")
    print("3 - REMOVER CONTATO")
    print("4 - ENCERRAR PROGRAMA")
    escolha = int(input("Escolha uma das opções: "))
    # Condicionais para chamar as respectivas funções criadas anteriormente conforme a escolha do usuário.
    if escolha == 1:
        print(f"ID do contato: {id_global}")
        id_global += 1
        cadastrar_contato(id_global)
    elif escolha == 2:
        consultar_contato()
    elif escolha == 3:
        remover_contato()
    elif escolha == 4:
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida")
