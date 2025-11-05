#Solicitar ao usuário que informe a hora atual (apenas o numero da hora)
hora = int(input("Digite a hora atual (0 a 23): "))

#Estrutura condicional 
if hora <= 12:
    print("Bom dia!")
elif hora > 12 and hora < 18:
    print("Boa tarde!")
else:
   print("Boa noite!")
