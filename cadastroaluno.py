#Objetivo criar um programa de gerenciamento de notas e mostrar o uso de len(), append(),sum(), remove()

#Lista vazia para armazenar as notas 
notas= []

print("   Gerenciador de notas   ")

while True:
    print("\nMenu de opções:")
    print("1 - Adicionar nota")
    print("2 - Remover nota")
    print("3 - Mostrar todas as notas")
    print("4 - Monstrar a quantidade e media das notas")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    #se a opcao for igual a 1, Adicionar nota
    if opcao == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("Nota adicionada com sucesso!")
    
    #remove nota
    elif opcao == 2:
        if len(notas) == 0:
            print("Não há notas para remover!")
        else:
            print("Notas atuais: ",nota)
            remover = float(input("Digite a nota que deseja remover: "))
            if remover in notas:
                notas.remove(remover)
                print(f"Nota {remover} removida com sucesso.")
            else:
                print("Essa nota não está na lista.")

    #mostrar as notas
    elif opcao == 3:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada ainda.")
        else:
            print("Notas cadastradas: ",notas)
    
    #mostrar quantidade e media
    elif opcao == 4:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada ainda para calcular a média.")
        else:
            quantidade = len(notas)
            soma = sum(notas)
            media = soma/quantidade
            print(f"Quantidade de notas: {quantidade}")
            print(f"Soma das notas: {soma:.2f}")
            print(f"Média da turma: {media:.2f}")

            if media >= 7:
                print("A turma está com bom desempenho!")
            else:
                print("A turma precisa melhorar.")

    #sair
    elif opcao == 5:
        print("Encerrando o programa, Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")    