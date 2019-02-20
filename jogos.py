import forca
import adivinhacao
import os


def escolhe_jogo():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Bem-vindo ao Jogos da Alura!")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("(1) - Forca")
    print("(2) - Adivinhe o número")

    jogo = int(input("Selecione um jogo: "))

    if(jogo == 1):
        os.system('cls')
        forca.jogar()
    elif(jogo == 2):
        os.system('cls')
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
