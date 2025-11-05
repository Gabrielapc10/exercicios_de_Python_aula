usuario1 = input("cadastre seu usuario ? ")
senha1 = input("cadastre sua senha?")
admin = input("Qual nivel se acesso: 1=adiministrador 2=comum.")

usuario = input("Qual seu usuario ? ")
senha = input("Qual sua senha?")


if senha1 == senha and usuario1 == usuario:
         print("Senha e usuario corretos")
         if admin == "1":
             print("Bem vindo administrador")
         elif admin == "2":
             print("Bem vindo usuario comum")
else:
    print("Senha ou usuario incorretos")            