nomes = []
salarios = []

while True :
    nome = input("Digite o nome do funcionario (ou 'sair' para encerrar)")

    if nome == "sair":
        print("Programa finalizado!")
        break

    nomes.append(nome)

    salario = float(input("Digite o salario do funcionario"))

    salarios. append(salario)

print(f"O total de funcionarios cadastrados é: {len(nomes)}")
print(f"A media salarial dos funcionarios é: {sum(salario)/len(salarios)}")
print(f"O maior salario é: {max(salarios)}.")
print(f"O menor salario é: {min(salarios)}.")