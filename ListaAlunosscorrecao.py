nomes = []

while True:
    n = input("Digite o nome que deseja (digite 'Sair' para encerrar):").lower()
    if n == "Sair":
        print("Encerrando o programa!")
        break
    nomes.append(n)

print(f"A quantidade de nomes informados {len(nomes)}")
print(f"A lista completa de nomes é: {nomes}.")