cliente = {
    "nome": input("Qual seu nome: "),
    "telefone": input("Seu telefone: "),
    "Saldo": float(input("Digite seu saldo inicial: "))
}

carros = [{"marca": "volkswagen" ,"modelo": "Gol","preco": 83038},
          {"marca": "fiat","modelo":"argo" ,"preco": 93980},
          {"marca": "toyota","modelo": "Corola","preco": 165890},
          {"marca": "ford","modelo": "ka","preco": 48794},
          {"marca": "honda","modelo": "civic","preco": 24225}]

carros_aluguel = [( "honda", "fiat")]

carro_venda = [("toyota","volkswagen","ford")]

def menu():
    print("---Concessionaria Gabriela---")
    print("1 - Ver saldo")
    print("2 - Vender carro ")
    print("3 - Alugar carro")
    print("4 - Comprar carro ")
    print("5 - Sair")

def vender_carros():
 
    marca = input("Digite a marca do carro: ")

    if marca not in carros:
        print("Esse carrro não tem.")
        return
    preco=carros[marca]

    proposta = preco*0.12

print(f"valor original :{preco:.2f}")
print(f"Proposta de compra: {proposta:.2f}")

sim = input("Deseja vender o carro? (sim ou nao).")

if sim == sim:
    print("carro vandido.")
else:
    print("cancelado.")




  

    


    