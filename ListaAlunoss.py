nomes = []
print("-Cadastro nomes de Alunos-")

while True: 
    print("\nMenu de opções:")
    print("1 - adicionar o nome dos alunos")
    print("2 - lista completa")
    print("3 - Quantidade de nomes")
    print("4 - sair")

    opcao =  int(input("Escolha uma ação:"))
    
    if opcao == 1:
        nome = str(input("Nome do aluno:"))
        nomes.append(nome)
        print("Nome cadastrado!")
       
    elif opcao == 2:
        if len(nomes) == 0:
            print("Nenhum nome cadastrado.")
        else:
            print("Nomes cadastrados.",nomes)
    elif opcao == 3:
        if len(nomes) == 0:
           print("nenhum nome cadastrado") 
        else:
            quantidade=len(nomes)
            print(f"Quantidade de nomes: {quantidade}")

    elif opcao == 4:
        print("Fim") 
        break
    else:
        print("Opção Inválida")
        
             
