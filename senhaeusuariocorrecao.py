print(" Cadastro de usuario ")
usuario1 = input("cadastre seu usuario ? ")
senha1 = input("cadastre sua senha?")

print("\nUsuario cadastrado com sucesso! \nAgora faça o login para acessar o sistema.\n")
print("\n Login")

usuario = input("Qual seu usuario ? ")
senha = input("Qual sua senha?")


if senha1 == senha and usuario1 == usuario:
         print(f"Senha e usuario corretos, Seja bem vindo(a) {usuario}")

         nivel = int(input("Digite o nivel de acesso (1 para administrador, 2 para comum): "))
        
         if nivel == 1:
                 print(f"Bem vindo(a), administrador {usuario}!")
         elif nivel == 2:
                 print(f"Bem vindo(a), usuario {usuario}!")
         else:
             print("Nivel de acesso invalido.")

else:
    print("Senha ou usuario incorretos")