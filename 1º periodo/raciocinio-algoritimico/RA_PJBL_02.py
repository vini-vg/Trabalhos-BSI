# Programa: Vending Machine
# Autor: Rafael Galafassi, Vinicius Costa, Marcos Vincius e Vinicius Viana
# Data de criação: 07/06/2023
# Versão: 2.0
# Descrição: Programa que simula uma máquina de vendas.
# Observação: letras maiúsculas e números de 0 à 9 serão a única forma de entrada.

# Matriz para armazenar os produtos, quantidades e os preços
produtos = [["1", 10, 2.5],["2", 5, 3.0],["3", 8, 2.0]]
relatorios_de_pagamento = []  # Matriz para armazenar informações de vendas: Quantidade de produto X vendido, valor total da compra. Se for em PIX, Quantidade de produto X vendido, valor total da compra e telefone do consumidor.
pagamentos_dinheiro = [] # Lista para armazenar os pagamentos em dinheiro
pagamentos_pix = [] # Lista para armazenar os pagamentos via PIX
# Matriz para armazenar a quantidade de dinheiro por tipo (cédulas e moedas)
# Moedas de 0.25, 0.5, 1.0 // Cédulas de 2, 5, 10 // valor_total_pix 
quantidade_dinheiro = [[0, 0, 0],[0, 0, 0],[0]]
numeros_validos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def login(usuario, senha):
     # Implementar a lógica de autenticação
    if usuario == "Administrador" and senha == "1234":
        print("Login do administrador bem-sucedido.")
    else:
        print("Usuário ou senha inválidos.")


def visualizar_produtos():
    print("Produtos disponíveis:")
    for produto in produtos:
        nome = produto[0]
        quantidade = produto[1]
        preco = produto[2]
        print(f"Nome: {nome} - Quantidade: {quantidade} - Preço: {preco}")
    

def adicionar_estoque(refrigerante, quantidade):
    # Implementar a lógica para adicionar a quantidade especificada ao estoque do refrigerante
    
    for produto in produtos:
        if produto[0] == refrigerante:
            produto[1] += quantidade
            
            print("Foram adicionadas", quantidade, "novas unidades de", refrigerante, "ao estoque.")
            return
    
    print("Produto não encontrado no estoque, ou quantidade invalida, digite novamente!")

def visualizar_quantidade_dinheiro():
    print("Quantidade de dinheiro por tipo:")
    print("Moedas:")
    print(f"0.25: {quantidade_dinheiro[0][0]}")
    print(f"0.5: {quantidade_dinheiro[0][1]}")
    print(f"1.0: {quantidade_dinheiro[0][2]}")
    print("Cédulas:")
    print(f"2: {quantidade_dinheiro[1][0]}")
    print(f"5: {quantidade_dinheiro[1][1]}")
    print(f"10: {quantidade_dinheiro[1][2]}") 
    print("PIX:")
    print("valor total pix = ", quantidade_dinheiro[2][0])

def modificar_quantidade_dinheiro():
    print("Modificar quantidade de dinheiro por tipo:")
    for ContDinheiro in range(3):
        print("Moedas:")
        quantidade_dinheiro[0][ContDinheiro] = int(input("Digite a nova quantidade de moedas de 25, 50 centavos e 1 real, respectivamente: "))
        print("Cédulas:") 
        quantidade_dinheiro[1][ContDinheiro] = int(input("Digite a nova quantidade de cédulas de 2, 5 e 10 reais, respectivamente: "))

def visualizar_relatorios():
    # Relatório de vendas
    print("Relatório de pagamentos:")
    pass

def atualizar_quantidade_dinheiro(valor_inserido):
    # Implementar a lógica para atualizar a quantidade de dinheiro, por exemplo o usuario recebeu troco, tem que diminuir e se comprou tem que aumentar
    pass

def realizar_pagamento(refrigerante, quantidade, opcao_pagamento):
    # Implementar a lógica para pagamento dos produtos, via pix ou dinheiro.
    if opcao_pagamento == 1:
        preco_unitario = 0

        if refrigerante == "1":
            preco_unitario = produtos[0][2]
            produtos[0][1] = produtos[0][1] - quantidade
        elif refrigerante == "2":
            preco_unitario = produtos[1][2]
            produtos[1][1] = produtos[1][1] - quantidade
        elif refrigerante =="3":
            preco_unitario = produtos[2][2]
            produtos[2][1] = produtos[2][1] - quantidade

        valor_total = quantidade * preco_unitario

        telefone = int(input("Digite o numéro de telefone referente ao seu pix: "))
        valor_pago = 0 
        print("Valor total da compra: ", valor_total)
        valor_pago = float(input("Digite o valor a ser pago: "))

        if valor_pago == valor_total:
            pagamentos_pix.append(valor_pago)
            pagamentos_pix.append(telefone)
            print(pagamentos_pix)
        elif valor_pago != valor_total:
            print("Insira o valor correto!! >:(")
            realizar_pagamento(refrigerante, quantidade, opcao_pagamento)
        return
def main():
    while True:
        print("Bem-vindo(a) ao Sistema de Pagamentos da Máquina de Venda Automática!")
        print("Selecione uma opção:")
        print("1. Administrador")
        print("2. Consumidor")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            algarismos_validos = [1, 2, 3, 4, 5]
            usuario = "Administrador"
            senha = input("Senha: ")
            login(usuario,senha)
            print("Selecione uma opção:")
            print("1. Visualizar produtos no estoque")
            print("2. Adicionar produtos no estoque")
            print("3. Visualizar quantidade de dinheiro")
            print("4. Modificar quantidade de dinheiro")
            print("5. Visualizar relatórios de pagamento")
            opcao_adm = int(input("Digite uma opção:"))
            if opcao_adm == 1:
                visualizar_produtos()
            elif opcao_adm == 2:
                refrigerante = input("Digite o nome do refrigerante: ")
                quantidade = int(input("Digite a quantidade que quer adicionar ao estoque: "))
                adicionar_estoque(refrigerante, quantidade)
            elif opcao_adm == 3:
                visualizar_quantidade_dinheiro()
            elif opcao_adm == 4:
                modificar_quantidade_dinheiro()
            elif opcao_adm == 5:
                visualizar_relatorios()
            else:
                opcao_adm != algarismos_validos
                print("Digite uuma opção válida!")
        elif opcao == "2":
            print("Login do consumidor bem-sucedido.")
            visualizar_produtos()
            refrigerante = (input("Digite o número do refrigerante desejado: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            print("Selecione uma opção de pagamento:")
            print("1. PIX")
            print("2. Dinheiro")
            opcao_pagamento = int(input("Opção de pagamento: "))
            realizar_pagamento(refrigerante, quantidade, opcao_pagamento)

        elif opcao == "3":
            print("Obrigado por utilizar o Sistema de Pagamentos da Máquina de Venda Automática!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

main()