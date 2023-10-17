def input_set(prompt):
    while True:
        try:
            values = input(prompt).split()
            return set(map(int, values))
        except ValueError:
            print("Digite os números dos elementos separados por espaço.")

def main_menu():
    set_a = set()
    set_b = set()
    
    while True:
        print("\nMenu Principal:")
        print("1. Alterar Conjunto A")
        print("2. Alterar Conjunto B")
        print("3. Realizar Operações")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            set_a = input_set("Digite os elementos do Conjunto A separados por espaço: ")
        elif choice == '2':
            set_b = input_set("Digite os elementos do Conjunto B separados por espaço: ")
        elif choice == '3':
            operations_menu(set_a, set_b)
        elif choice == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

def operations_menu(set_a, set_b):
    while True:
        print("\nOperações:")
        print("a) União")
        print("b) Intersecção")
        print("c) Diferença")
        print("d) Produto Cartesiano")
        print("e) Verificação de Subconjunto")
        print("f) Sair para o Menu Principal")
        
        choice = input("Escolha uma operação: ")
        
        if choice == 'a':
            print("União:", set_a | set_b)
        elif choice == 'b':
            print("Intersecção:", set_a & set_b)
        elif choice == 'c':
            print("Diferença (A - B):", set_a - set_b)
        elif choice == 'd':
            cartesian_product = {(x, y) for x in set_a for y in set_b}
            print("Produto Cartesiano:", cartesian_product)
        elif choice == 'e':
            sub_menu(set_a, set_b)
        elif choice == 'f':
            break
        else:
            print("Escolha uma operação válida.")

def sub_menu(set_a, set_b):
    while True:
        print("\nVerificação de Subconjunto:")
        print("a) A é subconjunto de B?")
        print("b) B é subconjunto de A?")
        print("c) Sair para Operações")
        
        choice = input("Escolha uma opção: ")
        
        if choice == 'a':
            if set_a.issubset(set_b):
                print("A é subconjunto de B.")
            else:
                print("A não é subconjunto de B.")
        elif choice == 'b':
            if set_b.issubset(set_a):
                print("B é subconjunto de A.")
            else:
                print("B não é subconjunto de A.")
        elif choice == 'c':
            break
        else:
            print("Escolha uma opção válida.")