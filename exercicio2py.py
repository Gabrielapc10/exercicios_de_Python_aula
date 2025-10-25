valor = int(input("Digite o valor de compra: "))

if valor < 100:
    print(input("Não há desconto."))
elif valor > 100:
    print(input("10% de desconto aplicado!", int(valor)*0.9))


