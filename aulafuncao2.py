def cadastrar_produto(estoque):
    nome = input("Nome do produto: ")
    qtd = int(input("quantidade: "))
    estoque[nome] = qtd
    print("Produto cadastrado")

def vender(estoque):
    nome = input("Produrto para vender: ")
    if nome in estoque and estoque[nome] > 0:
        estoque[nome] -= 1
        print("Venda realizada!")
    else:
        print("Produto indisponivel!")

def mostrar(estoque):
    print("\n---Estoque---")
    for p,q in estoque.items():
        print(f"{p}:{q}")

def menu():
    estoque = {}

    while True:
        print("\n1 - Cadastrar \n2 - Vender \n3 - Mostrar\n4 - Sair")
        
        op = int(input("Escolha: "))

        match op:
            case 1:
                cadastrar_produto(estoque)
            case 2:
                vender(estoque)
            case 3:
                mostrar(estoque)
            case 4:
                print("Esncerrando o sistema....")
                break

menu()