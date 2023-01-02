import forca
import adivinhacao
import os


def valid_entrada_int(entrada):
    if entrada.strip() == "" or entrada.strip().isalpha():
        entrada = 404
    else:
        entrada = int(entrada)
    return entrada


def msg_inicial():
    print('--------------------------------')
    print('--        Hub de Jogos        --')
    print('--------------------------------')


def set_jogo():
    jogo = input('Escolha o Jogo\n(1)-Forca\n(2)-Adivinhação')
    jogo = valid_entrada_int(jogo)

    if jogo == 1:
        print('Inicializando Forca')
        forca.forca()
    elif jogo == 2:
        print('Inicializando Adivinhação')
        os.system('cls')
        adivinhacao.adivinhacao()
    else:
        print('Jogo inválido')
        return set_jogo()


def hub():
    msg_inicial()
    set_jogo()


if __name__ == "__main__":
    hub()