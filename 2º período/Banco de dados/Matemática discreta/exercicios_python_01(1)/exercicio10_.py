def adicionar_elementos_A(A, quantidade):
    quantidade = int(input("Digite a quantidade de elementos:"))

    for _ in range(quantidade):
        elemento = ("Digite o elemento para ser adicionado: ")
        A.add(elemento)

def adicionar_elementos_B(B, quantidade):
    quantidade = int(input("Digite a quantidade de elementos:"))
    
    for _ in range(quantidade):
        elemento = ("Digite o elemento para ser adicionado: ")
        B.add(elemento)

def menu_principal():

    A = set()
    B = set()

    while True:
        print("\nMenu Principal")
        print("1. Dê um valor ao conjunto A")
        print("2. Dê um valor ao conjunto B")
        print("3. Realizar operações")
        print("4. Encerrar processos")

        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print(adicionar_elementos_A)
        elif escolha == "2":
            adicionar_elementos_B
        elif escolha == "3":
            menu_operacoes(A, B)
        elif escolha == "4":
            print("Encerrando o programa")
        else:
            print("Escolha uma opção válida")

def menu_operacoes(A, B):

    while True:
        print("\nMenu de Operações")
        print("1. União")
        print("2. Intercecção")
        print("3. Diferença")
        print("4. Produto Cartesiano")
        print("5. Verificação de subconjunto")
        print("6. Voltar para o menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("União", A | B)
        elif escolha == "2":
            print("Intercecção", A.intersection(B))
        elif escolha == "3":
            print("Diferença", A - B)
        elif escolha == "4":
            produto_cartesiano = {(x,y) for x in A for y in B}
            print("Produto cartesiano", produto_cartesiano )
        elif escolha == "5":
            sub_menu(A, B)
        elif escolha == "6":
            break
        else:
            print("Escolha uma opção válida")

def sub_menu(A, B):

    while True:
        print("\nVerificando Subconjuntos: ")
        print("1. A é subconjunto de B?")
        print("2. B é subconjunto de A")
        print("3. Voltar para as operações")
        
        escolha = input("Esolha uma opção: ")

        if escolha == "1":
            if A.issubset(B):
                print("É subconjunto de B")
            else:
                print("Não é subconjunto de B")
        elif escolha == "2":
            if B.issubset(A):
                print("É subconjunto de A")
            else:
                print("Não é subconjunto de A")
        elif esolha == "3":
            break
        else:
            print("Escolha uma opção válida")
        
menu_principal()

        