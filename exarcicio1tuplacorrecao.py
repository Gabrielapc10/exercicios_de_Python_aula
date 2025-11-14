#nomes = ("ana", "Breno", "carlos", "daniela", "enzo")

nomes = ()#Tupla vazia

print("-Lista de Nomes-")
#print(nomes) mostra a tupla com os nomes

#estrutura de repeticao que vai rodar 5 vezes pedindo nomes
for  i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes += (nome, ) # adiciona os nomes informados pelo usuario a tupla

print(f"Nomes cadastrados: {nomes}")
print(f"Primeiro nome: {nomes[0]}")
print(f"Ultimo nome: {nomes[-1]}")
print(f"A quantidade total de nomes: {len(nomes)}")