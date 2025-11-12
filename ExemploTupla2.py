#criacao de programa que permita que o usuario consulte o preco de um produto digitando o nome.

#Duas tuplas paralelas: uma com os nomes dos produtos e a outra com os preços
produtos = ("arroz","feijão","macarrão","leite","pão","ovo")
precos = (5.50, 6.4, 9.5, 2.0, 3.89, 9.0)

#Exibe a lista completa de produtos com seus preços 
print("\n    Lista de Produtos    ")
for i in range(len(produtos)):
    #Percorre as posiçoes (0 até 5) e exibe o produto e o preço correspondente
    print(f"{produtos[i]} - R$ {precos[i]:.2f}")

#Inicia um loop pra permitir varias consultas do usuario
while True:
    nome = input("\nDigite o nome produto para ver o preço (ou 'sair'): ").lower()
    #Método .lower() tranforma o texto em minusculas para evitar o erro de comparaçao 

    #se o usuario digitar 'sair', o programa termina
    if nome == "sair":
        print(f"Programa encerrado.")
        break
    
    #verifica se o produto existe dentro da tupla 'produtos'
    if nome in produtos:
        indice = produtos.index(nome) #se o produto existe, encontramos sua posicao em index()
        #index() serve para retornar a posição (indice) o nome foi encontrado dentro da tupla
        print(f"O preço de {nome} é R$ {precos[indice]:.2f}.")
    else:
        print("Produto não encontrado.")