print("\n   LOJA TECHSTORE SENAI   ")
valor=float(input("Digite o valor total da compra(R$):  "))
formapagamento = input("Forma de pagamento (Dinheiro/cartão debito/cartão crédito/pix): ")

if formapagamento == "dinheiro":
    total = valor*0.90
    print("Pagamento á vista em dinheiro. Desconto de 10% aplicado!")
elif formapagamento == "pix":
    if valor >= 1000:
        total = valor*0.85
        print("Pagamento via pix: Desconto de 15% aplicado!")
    elif valor >= 500 and valor < 1000:
        total = valor*0.90
        print("Pagamento via pix: Desconto de 10% aplicado!")
    else:
        total = valor*0.95
        print("Pagamento via pix: Desconto de 5% aplicado!")
elif formapagamento == "Débito":
    total = valor 
    print("Pagamento à vista no cartão de débito!")
elif formapagamento == "credito":
    parcelas = int(input("Em quantas vezes deseja parcelar? "))
    if parcelas <= 3:
        total = valor 
        print("Parcelamento em até 3x sem juros!")
    elif 4 <= parcelas <= 6:
        total = valor*1.10
        print("Parcelamento de 4 a 6x com 10% de juros!")
    else:
        total = valor*1.20
        print("Parcelamento acima de 6x com 20% de juros!")
else:
    print("Forma de pagamento inválida! Tente novamente usando outra opção.") 

print(f"Valor final a pagar : R$ {total:.2f}")
