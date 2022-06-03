import random


def jogar():
    print("*************************************")
    print("***Bem vindo ao jogo - advinhação!***")
    print("*************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nídel de dificuldade?")
    print("(1)-> Fácil (2)-> Médio (3)->Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Erro: nivel mau inserido.")


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!")
            continue
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if total_de_tentativas in range(1, total_de_tentativas + 1):
        print("O número secreto era: {}".format(numero_secreto))

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()