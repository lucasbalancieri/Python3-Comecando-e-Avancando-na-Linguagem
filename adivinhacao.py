import random
import sys
import os
import time

import main


def msg_inicial():
    print('------------------------------------')
    print('- Bem vindo ao jogo de Adivinhação -')
    print('-    Descubra o número secreto     -')
    print('------------------------------------')


def set_dificuldade():
    dificuldade = input('Selecione a dificuldade:\n(1) Fácil\n(2) Normal\n(3) Difícil\n')
    dificuldade = main.valid_entrada_int(dificuldade)

    if dificuldade < 1 or dificuldade > 3:
        os.system('cls')
        print('Dificuldade inválida, digite novamente')
        return set_dificuldade()
    else:
        os.system('cls')
        return dificuldade


def set_tentativas(dificuldade):
    qtd_tentativas = 0
    if dificuldade == 1:
        qtd_tentativas = 20
    elif dificuldade == 2:
        qtd_tentativas = 10
    elif dificuldade == 3:
        qtd_tentativas = 5
    return qtd_tentativas


def palpite(rodada, qtd_tentativas):
    print('Rodada {} de {}'.format(rodada, qtd_tentativas))
    palpite_jogador = input('Digite seu palpite entre 1 e 100: ')
    palpite_jogador = main.valid_entrada_int(palpite_jogador)

    palpite_jogador = int(palpite_jogador)  # Converter para int
    os.system('cls')

    if palpite_jogador < 1 or palpite_jogador > 100:
        print('Tentativa inválida, digite novamente')
        return palpite(rodada, qtd_tentativas)
    else:
        return palpite_jogador


def validar_palpite(palpite_jogador, numero_secreto):
    palpite_certo = palpite_jogador == numero_secreto
    palpite_maior = palpite_jogador > numero_secreto
    palpite_menor = palpite_jogador < numero_secreto

    if palpite_certo:
        print('Acertou!\nVocê venceu!')
        return True
    else:
        if palpite_maior:
            print('{} é MAIOR do que o número secreto!'.format(palpite_jogador))
        elif palpite_menor:
            print('{} é MENOR do que o número secreto!'.format(palpite_jogador))


def pontuacao(pontos, erro_acumulado):
    pontuacao_final = abs(pontos - erro_acumulado)
    return pontuacao_final


def game_over(rodada, qtd_tentativas, numero_secreto):
    if rodada > qtd_tentativas:  # Se a rodada for maior do que o numero de tentativas, significa que o usuário perdeu.
        os.system('cls')
        print('Voce perdeu!\nO numero secreto era: {}'.format(numero_secreto))
        print('Fim do Jogo!')
    else:
        print('Fim do Jogo!')


def novo_jogo():
    op = input('\n\nObrigado por jogar!\n(1) Jogar Novamente\n(2) Menu Principal\n(0) Sair')
    op = main.valid_entrada_int(op)

    if op == 1:
        os.system('cls')
        adivinhacao()
    elif op == 2:
        os.system('cls')
        main.hub()
    elif op == 0:
        os.system('cls')
        sys.exit()
    else:
        print('Opção inválida, voltando ao menu principal.')
        time.sleep(2)
        os.system('cls')
        main.hub()


def adivinhacao():
    erro_acumulado = 0
    rodada = 1
    pontos = 1000
    lista_palp_errados = []

    msg_inicial()
    dificuldade = set_dificuldade()
    qtd_tentativas = set_tentativas(dificuldade)
    numero_secreto = random.randrange(1, 101)

    while rodada <= qtd_tentativas:
        palpite_jogador = palpite(rodada, qtd_tentativas)
        erro_acumulado = erro_acumulado + abs((numero_secreto-palpite_jogador))

        if validar_palpite(palpite_jogador, numero_secreto):
            print('Pontuação final: ', pontuacao(pontos, erro_acumulado))
            break
        else:
            lista_palp_errados.append(palpite_jogador)
            print('Palpites Errados: ', lista_palp_errados)
        rodada += 1

    game_over(rodada, qtd_tentativas, numero_secreto)
    novo_jogo()


if __name__ == "__main__":
    adivinhacao()