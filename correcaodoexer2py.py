#Solicitar o valor da compra e guardar na variavel
valor = float(input("Digite o valor de compra: "))
#Verifica se o valor da compra é maior que 100
if valor > 100:
    #Aplica o desconto de 10%, multiplicando o valor por 0.9 o valor 
    valorfinal = valor * 0.9
    print("10% de desconto aplicado! \n O valor com desconto é: ",valorfinal)
else:
    #caso contrario, mantem o valor original
    valorfinal = valor
    print("Não há desconto.\n Valor da compra sem desconto é: ",valorfinal)

 
