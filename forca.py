import random
import os
import sys

import main


def msg_inicial():
    print('--------------------------------')
    print('-  Bem vindo ao jogo da Forca  -')
    print('--------------------------------')


def set_palavra():
    arquivo = open("palavras.txt", "r")  # Abrir arquivo
    palavras = []
    for linha in arquivo:
        linha = linha.strip()  # Remove os \n do final de cada palavra
        palavras.append(linha)  # Coloca cada linha como uma palavra dentro da lista palavras
    arquivo.close()  # Fechar arquivo

    numero = random.randrange(0, len(palavras))  # Escolhe um número random dentro do range de index da lista palavras
    palavra_secreta = palavras[numero].upper()  # Define a palavra secreta com base no index da lista palavras representado pela variável numero.
    return palavra_secreta


def check_letra(palavra_secreta):
    return ["_" for letra in palavra_secreta]  # append '-' na lista para cada letra na palavra secreta


def palpite():
    palpite_jogador = input('Letra:\t')
    if palpite_jogador.strip() == "" or palpite_jogador.isdigit() or len(palpite_jogador) != 1:
        print('Palpite inválido')
        return palpite()
    else:
        palpite_jogador = palpite_jogador.strip().upper()  # Retira espaços no inicio e final da entrada ex:' abc '.strip() retorna 'abc'
        return palpite_jogador


def set_pos_letra(palpite_jogador, palavra_secreta, qtd_letras):
    index = 0
    for letra in palavra_secreta:
        if palpite_jogador == letra:
            qtd_letras[index] = letra
        index += 1


def msg_win(palavra_secreta):
    print('Parabéns! A palavra é {}'.format(palavra_secreta))


def msg_lose(palavra_secreta):
    print("Você Perdeu!\nA palavra era {}".format(palavra_secreta))


def novo_jogo():
    op = input('\n\nObrigado por jogar!\n(1) Jogar Novamente\n(2) Menu Principal\n(0) Sair')
    op = int(op)

    if op == 1:
        os.system('cls')
        forca()
    elif op == 2:
        os.system('cls')
        main.hub()
    elif op == 0:
        os.system('cls')
        sys.exit()
    else:
        print('Opção inválida, voltando ao menu principal.')
        os.system('cls')
        main.hub()


def forca():
    lose = False
    win = False
    erros = 0
    lista_palp_errados = []

    msg_inicial()
    palavra_secreta = set_palavra()
    qtd_letras = check_letra(palavra_secreta)
    print(qtd_letras)

    while not win and not lose:
        palpite_jogador = palpite()
        print(palpite_jogador)

        if palpite_jogador in palavra_secreta:
            set_pos_letra(palpite_jogador, palavra_secreta, qtd_letras)
            print(qtd_letras)
        else:
            print('A palavra não tem a letra {}'.format(palpite_jogador))
            lista_palp_errados.append(palpite_jogador)
            print('Letras Erradas: ', lista_palp_errados)
            erros += 1

        lose = erros == 6
        win = '_' not in qtd_letras

    if win:
        msg_win(palavra_secreta)
    else:
        msg_lose(palavra_secreta)

    novo_jogo()


if __name__ == "__main__":
    forca()