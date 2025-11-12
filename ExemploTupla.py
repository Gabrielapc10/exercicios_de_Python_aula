numeros = () #Criação de tupla com o nome que ira guadar numeros fornecidos pelo usuario 

#Estrutura de repetição para permitir que o usuario digite vários números
while True:
    n = int(input("Digite um numero (ou -1 para sair): "))
    #Se o usuario digitar -1, o laço é interrompido (break)
    if n == -1:
        break
    numeros += (n,) #como tuplas são imutaveis não usamos append(), em vez disso criamos uma  nova tupla com o número adicionado  

#Após sair do loop, vrificamos se a tupla está vazia ou não
if len(numeros) > 0:
    print("\n   Resultados   ")
    print(f"Número digitados: {numeros}")
    print(f"Quantidade: {len(numeros)}")
    print(f"Soma: {sum(numeros)}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

    media = sum(numeros)/len(numeros)

    if media >= 50:
        print(f"Média: {media:.2f} -> Alta!")
    else:
        print(f"Média: {media:.2f} -> Baixa!")

else:
    print("Nenhum número foi adicionado!")
