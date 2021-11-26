import random


print("**********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.random() * 100)
total_de_tentativas = 3


while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu numero: ")
    print("Você digitou " , chute)
    chute = int(chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1




print("Fim do jogo")