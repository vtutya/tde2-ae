import os

clientes = []

def menu():
    print("*" * 35)
    print("\n1. Cadastrar")
    print("2. Consulta")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Sair")
    print("*" * 35) 
    
    while True:
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            cadastrar()
            break
        elif escolha == 2:
            consultar()
            break
        elif escolha == 3:
            alterar()
            break
        elif escolha == 4:
            excluir()
            break
        elif escolha == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")    


def cadastrar():
    print("Cadastro de clientes")
    print("*" * 35)
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco
    }
    clientes.append(cliente)
    os.system("cls" if os.name == "nt" else "clear")
    print("\nCliente cadastrado com sucesso!")

    print("Digite 1 para cadastrar outro cliente ou 2 para voltar ao menu")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        menu()

def consultar():
    print("Consulta de clientes")
    print("*" * 35)
    print("1. Realizar consulta")
    print("2. Voltar ao menu")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        consulta()
    elif escolha == 2:
        menu()
  


def consulta():
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Nome: ", cliente["nome"])
            print("CPF: ", cliente["cpf"])
            print("Telefone: ", cliente["telefone"])
            print("Endereço: ", cliente["endereco"])
            menu()

def alterar():
    print("Alterar dados do cliente: ")
    print("*" * 35)
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("1. Nome")
            print("2. CPF")
            print("3. Telefone")
            print("4. Endereço")
            escolha = int(input("Escolha o campo que deseja alterar: "))
            if escolha == 1:
                cliente["nome"] = input("Digite o novo nome: ")
            elif escolha == 2:
                cliente["cpf"] = input("Digite o novo CPF: ")
            elif escolha == 3:
                cliente["telefone"] = input("Digite o novo telefone: ")
            elif escolha == 4:
                cliente["endereco"] = input("Digite o novo endereço: ")
            print("Dados alterados com sucesso!")
            menu()


def excluir():
    print("Excluir cliente: ")
    print("*" * 35)
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
            menu()

def sair():
    os.system("cls" if os.name == "nt" else "clear")
    print("Saindo...")
                

menu()                