meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Julho", "Junho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print("-Meses do Ano-")

while True:
    numero = int(input("Digite um número entre 1 e 12 para saber o mês correspondente: (Informe -1 para sair)"))

    if numero == -1:
        print("Encerrando o sistema!")
        break

    if numero >= 1 and numero <= 12:
        print(f"O mes correspondente é: {meses[numero - 1]}")#serve para pegar o numero informado pelo usuario e subtrair -1 para pegar o valor certo
    else:
        print("Número invalido! Digite novamente entre 1 e 12...")
