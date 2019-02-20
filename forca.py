import random


def apresentacao():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Bem-vindo ao Jogo da Forca!")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


def encerramento():
    print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Fim de jogo")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


def carrega_palavras():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lower()
            palavras.append(linha)

    num_random = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num_random]
    return palavra_secreta


def init_letras(palavra):
    return ["_" for letra in palavra]


def mostra_letra(chute, palavra_secreta, letra_acertada):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letra_acertada[index] = letra

        index += 1


def imprimi_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era '{}'".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprimi_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    apresentacao()
    palavra_secreta = carrega_palavras()

    letras_acertadas = init_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ").lower().strip()

        if(chute in palavra_secreta):
            mostra_letra(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = (tentativas == 7)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("\n")

    if(acertou):
        imprimi_mensagem_vitoria()
    else:
        imprimi_mensagem_derrota(palavra_secreta)

    encerramento()


if(__name__ == "__main__"):
    jogar()
