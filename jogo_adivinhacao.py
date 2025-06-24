numero_secreto = 7
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} na tentativa {tentativas}.")
        break
else:
    print(f"Que pena! Suas {limite_tentativas} tentativas acabaram. O número correto era {numero_secreto}.")