print("\nCadastro de usuario\n")
usuario_cadastrado = input("Crie seu nome de usuario:").strip().lower()


print("\nUsuario cadastrado com sucesso!\n")

while True:
    senha_cadastrada = input("Crie uma senha de usuario: (máx. 8 caracteres): ").strip()
    
    if len(senha_cadastrada) <= 8:
        print("\nUsuario cadastrado com sucesso!\n")
        break
    else:
        print("Senha muito longa! Digite uma senha com até 8 caracteres.\n")


print("\n Login \n")
#Inicia um loop que vai se repetir enquanto a condicao for verdadeira
while True:#True é uma condicao booleana que sempre e verdadeira,logo esse loop será infinito
    nome = input("Usuario: ").strip().lower()
    senha = input("senha: ").strip()

    #condicao que faz uma comparacao para verificar se ambas condicoes sao verdadeiras 
    if nome == usuario_cadastrado and senha == senha_cadastrada:
        print(f"Login realizado com sucesso!\n Bem-vindo(a) {nome}")
        break #comando que interrompe imediatamente o loop
    else: 
        print("Usuario ou senha incorretos! Tente novamente...")
