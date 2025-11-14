pessoa = {}# criando um dicionario vazio chamado pessoa

#todos essses dados serão armazendados no dicionario
pessoa["nome"] = input("Digite o nome: ")#nome é chave e o que o usuario digitar será valor associado
pessoa["idade"] = int(input("Digite sua idade:"))#Idade é a chave que o usuario digitar será valor associado, usando int srá um numero inteiro
pessoa["cidade"] = input("Digite sua cidade: ")#Cidade é chave e o que o usuario digitar será valor associado

print("\n---Dados Cadastrados---")
#Percorrendo o dicionário usando itens(), chave = nome - valor = o conteúdo guardado
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")#Exibindo chave o valor formatados 
