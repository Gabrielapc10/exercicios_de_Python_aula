nomes = []
salarios = []

while True:
    print("1 - Nome e Salario")
    print("2 - Quantidade de funcionarios")
    print("3 - Media Salarial")
    print("4 - Maior e Menor Salario")
    print("5 - sair")
    

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = (input("Digite o nome: "))
        nomes.append(nome)
        print("Nome cadastrado.")
        salario = float(input("Digite o salario: "))
        salarios.append(salario)

    elif opcao == 2 :
        if len(nomes) == 0:
           print("nenhum nome e salario cadastrado") 
        else:
            quantidade=len(nomes)
            print(f"Quantidade de funcionarios: {quantidade}")
   
    elif opcao == 3:
        quantidade=len(salarios)
        soma = sum(salarios)
        media= soma/quantidade
        print("Media: ",soma)

    elif opcao == 4:
        print(f"Maior salario {max(salarios)}")
        print(f"Menor salario {min(salarios)}")

    elif opcao == 5:
        print("Fim") 
        break
    else:
        print("opcao invalida")



