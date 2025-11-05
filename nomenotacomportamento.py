nome = input("Qual o nome: ")
nota = float(input("Qual a nota: "))
comportamento = input("Qual o comportamento (bom/regular/ruim): ")
nota == comportamento

if nota >= 7:
    if comportamento == "bom":
        print("Aprovado com Mérito!")
    elif comportamento == "regular":
        print("Aprovado.")
    elif comportamento == "ruim":
        print("Aprovado, mas com observações.")
if nota < 7:
    if comportamento == "bom":
        print("Recuperação, mas com chance de melhora")
    else:
        print("Reprovado por nota e comportamento.")
        