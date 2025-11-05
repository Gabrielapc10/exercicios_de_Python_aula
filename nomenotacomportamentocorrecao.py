nome = input("Qual o nome: ")
nota = float(input("Qual a nota: "))
comportamento = input("Qual o comportamento (bom/regular/ruim): ")
nota == comportamento

if nota >= 7:
    if comportamento == "bom":
        print(f"{nome}, Aprovado com Mérito!")
    elif comportamento == "regular":
        print(f"{nome}, Aprovado.")
    elif comportamento == "ruim":
        print(f"{nome}, Aprovado, mas com observações.")
    else:
        print("Comportamento inválido! Digite: bom, regular ou ruim.")
else:
    if comportamento == "bom" and nota == 6:
        print(f"{nome}, Recuperação, mas com chance de melhora")
    elif comportamento == "ruim":
        print(f"{nome}, Reprovado por nota e comportamento.")
    else:
        print(f"{nome}, Reprovado!")