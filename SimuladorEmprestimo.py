# Simulador de Empréstimo Bancário

print("   Sistema de Análise de Credito   ")

#Solicitacao de entrada que serao armazenadas nas variaveis
nome = input("Nome do Cliente: ")
renda = float(input("Informe a renda mensal do cliente: R$ "))
valorpedido = float (input("Informe o valor do empréstimo desejado: R$"))
parcelas = int(input("Informe o número de parcelas: "))
historico = input("Possui nome sujo? (Sim/Não)")

#Calculo do valor da parcela
valorparcela = valorpedido/parcelas

#exibe um resumo inicial do cliente
print(f"\nCliente: {nome}")
print(f"Valor do empréstimo: R$ {valorpedido:.2f}")
print(f"Parcelas: {parcelas}x de R$ {valorparcela:.2f}")

#Verifica o primeiro se o nome está limpo
if historico == "sim":
    print("Emprestimo NEGADO! Nome com restrição.")
else:
    #Verifica se a parcela não ultrapassa 30% da renda
    if valorpedido > renda*0.3:
        print("Empréstimo NEGADO! Parcelas compremetem mais de 30% da renda.")
    else:
        #verifica valor do emprestimo em relacao à renda
        if valorpedido > renda*20:
            print("Empréstimo NEGADO! Valor solicitado muito alto para a renda informada.")
        elif renda >= 5000 and valorpedido <= 10000:
            print("Empréstimo APROVADO com taxa reduzida! Cliente parfil premium.")
        elif renda >= 3000 and renda < 5000:
            print("Enpréstimo APROVADO com taxa padrão.")
        else:
            print("Empréstimo APROVADO com taxa elevada (Cliente de risco).")

print("\n    ANÁLISE CONCLUÍDA   ")