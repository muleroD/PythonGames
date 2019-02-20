import random


def jogar():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    num_random = random.randrange(101)
    tentativas = 0
    pontos = 1000

    print("Selecione a dificuldade")
    print("(1) - Fácil \n(2) - Médio \n(3) - Difícil")
    nivel = int(input("Escolha um: "))

    print(num_random)

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    while (tentativas != 0):
        print("\nTentativas restantes: {}".format(tentativas), end="\n")
        print("Pontuação: ", pontos)

        chute = int(input("Digite um número: "))

        if(chute < 1 or chute > 100):
            print("Número deve ser entre 1 e 100")
            continue

        acerto = chute == num_random
        maior = chute > num_random
        menor = chute < num_random

        if(acerto):
            print("Acertou!!!")
            break
        else:
            tentativas = tentativas - 1
            pontos = pontos - abs(num_random - chute)
        if(maior):
            print("Errou - Chute muito alto")
        elif(menor):
            print("Errou - Chute muito baixo")

    print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Fim de jogo")
    print("Você fez {0} pontos".format(pontos))
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


if(__name__ == "__main__"):
    jogar()
