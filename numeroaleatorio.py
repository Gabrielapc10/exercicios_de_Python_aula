import random

secreto = random.randint(1, 100)
tentativas = 3

print("  Desafio do numero secreto   ")
print("  Desafio do numero secreto   ")


while tentativas > 0:
      chute = int(input("seu chute: "))

      if chute == secreto:
        print("Você acertou")
        break
      elif chute < secreto:
        print("chute muito baixo.")
      else:
         print("chute muito alto.")

      tentativas -= 1
      print(f"tentativas restantes {tentativas}\n")

if tentativas == 0:
     print(f"Acabaram as tentativas, o numero era: {secreto}")


