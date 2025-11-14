produto = [{"nome" : "cafe", "preço": 25.96, "categoria" : "alimentos", "estoque":30},
           {"nome": "detergente","Preco":2.99,"categoria": "limpeza", "estoque":50},
           {"nome": "sabao em po","Preco":17.99,"categoria": "limpeza", "estoque":5},
           {"nome": "pao","Preco":7.99,"categoria": "alimentos", "estoque":15}]

print("\n---Lista de Produto---")
for i in produto:
    print("--------------------")
    for chave, valor in i.items():#Serve para pegar chave e valor dentro do dicionário  
        print(f"{chave}:{valor}")
