#Exemplo de lista
#numeros = [10,20,30,40,50] #criei uma  lista com mumero inteiro (int)
#print(numeros)
#print(numeros[4]) #Acessando a lista e pegando p primeiro valor dela
#numeros[1] = 15
#numeros[3] = 25
#print(numeros)

##################

#Exemplo de Tupla
#print(coordenadas[0])
#print(coordenadas[1])
#coordenadas[0] = 13
#coordenadas[1] = 17
#print(coordenadas)

#append() - metodo que serve para adicionar um novo elemento ao final da lista
#remove() - metodo que remove um elemento da lista
#paises = ["Brasil","Argentina"]
#print(paises)
#paises.append("Russia")
#print(paises)
#paises.remove("Argentina")
#print(paises)

#if "Italia" in paises:
#    paises.remove("Brasil")
#    print(f"pais removido com sucesso. {paises}" )
#else:
#    print("Pais nao existe.")


numeros = [10,20,30]
print("Quantidade de numeros: ",len(numeros))

#len() - metodo que serve para contagem de caracteres, numeros, letras, palavras...
#sum() - metodo que serve para somar os elementos numericos

notas =[7.5, 8.5, 10]
print("soma das notas é: ",sum(notas))
print(f"A media da notas é: {sum(notas)/len(notas):.2f} ")

