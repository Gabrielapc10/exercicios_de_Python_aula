#Inicia um loop que vai se repetir enquanto a condicao for verdadeira
while True:#True é uma condicao booleana que sempre e verdadeira,logo esse loop será infinito
    nome = input("Usuario: ")
    senha = input("senha: ")

    #condicao que faz uma comparacao para verificar se ambas condicoes sao verdadeiras 
    if nome == "admin" and senha == "1234":
        print("Login realizado com sucesso!")
        break #comando que interrompe imediatamente o loop
    else: 
        print("Usuario ou senha incorretos! Tente novamente...")
        