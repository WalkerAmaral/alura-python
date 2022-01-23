import random

print("*********************************")
print("Bem-vinde ao jogo da adivinhação")
print("*********************************")

numero_secreto = random.randint(1,100)
print(numero_secreto)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1) or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        rodada = rodada - 1
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou " , chute)
    print()

    if(acertou):
        print("** Você acertou **")
        break
    else:
        if(maior):
            print("Você errou :( seu chute foi maior do que o número secreto")
        elif (menor):
            print("Você errou :( seu chute foi menor do que o número secreto")

print("Fim do jogo")
