# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19RP4IEl6NcutU4vMeNt-pK9lH9dP4VVi
"""



def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def exibir_menu():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    exibir_menu()
    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ['1', '2', '3', '4']:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado da soma é: {soma(x, y)}")
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtrai(x, y)}")
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplica(x, y)}")
        elif escolha == '4':
            print(f"O resultado da divisão é: {divide(x, y)}")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Por favor, selecione uma opção de 1 a 5.")

    print()  # Linha em branco para melhorar a legibilidade do menu

import random

def escolher_palavra():
    lista_de_palavras = ["microsoft", "mouse", "processador", "teclado", "notebook"]
    return random.choice(lista_de_palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(estagios[6 - tentativas])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_descobertas = ['_' for _ in palavra]
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")

    while tentativas > 0 and '_' in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Você tem {tentativas} tentativas restantes.")
        exibir_forca(tentativas)

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente uma diferente.")
            continue

        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    letras_descobertas[idx] = letra
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"Que pena! A letra '{letra}' não está na palavra.")

    if '_' not in letras_descobertas:
        print(f"\nParabéns! Você adivinhou a palavra: {palavra} \n\nObrigado por jogar!  ;D")
    else:
        exibir_forca(tentativas)
        print(f"\nVocê perdeu! A palavra era: {palavra} \n\nObrigado por jogar! ;D")

random.seed()
an
jogo_da_forca()
