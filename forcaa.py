import random # aleatório
import os # cores
import time  # importar time para o delay

TEMPO_DELAY = 1 # define o valor do delay de formar geral

def limpar_tela(): # cria a função limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')    # Limpa a tela do terminal usando -->
                                                        #cls no Windows e clear para outros sistemas


palavras = [
    'PYTHON', 'STRING', 'ALGORITIMOS', 'COMPUTADOR', 'TABELA' # define as palavras da forca
]

def jogar():
    limpar_tela() # limpa a tela utilizando a função já criada

    palavra = random.choice(palavras) # escolhe aleatóriamente a palavra com base na lista já criada
    letras_descobertas = [] # mostra os acertos de letras
    letras_erradas = [] # mostra os erros de letras
    tentativas = 4 # define o número de tentativas

    while tentativas > 0: 
        exibicao = ''
        for letra in palavra:
            if letra in letras_descobertas:
                exibicao += f"\033[32m{letra} \033[0m"  # Verde para letras certas
            else:
                exibicao += '_ '

        print("\033[34mJOGO DA FORCA 🕹️​\033[0m")  # Azul para o título
        print("Adivinhe a palavra!\n")
        print(f"\nPalavra: {exibicao.strip()}")
        print(f"\033[31mLetras erradas:\033[0m {' '.join(letras_erradas)}")  # Vermelho
        print(f"Tentativas restantes: {tentativas}")

        if all(letra in letras_descobertas for letra in palavra):
            print(f"\n\033[34mParabéns! Você acertou a palavra: {palavra}\033[0m") # Azul
            return

        tentativa = input("Digite uma letra: ").strip().upper()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("\033[33mDigite apenas UMA letra válida.\033[0m")  # Amarelo
            time.sleep(TEMPO_DELAY)  
            limpar_tela()
            continue

        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("\033[33mVocê já tentou essa letra.\033[0m")  # Amarelo
            time.sleep(TEMPO_DELAY)
            limpar_tela()
            continue

        if tentativa in palavra:
            print(f"\033[32mBoa! A letra '{tentativa}' está na palavra.\033[0m")  # Verde
            letras_descobertas.append(tentativa)
        else:
            print(f"\033[31mA letra '{tentativa}' não está na palavra.\033[0m")  # Vermelho
            letras_erradas.append(tentativa)
            tentativas -= 1

        time.sleep(TEMPO_DELAY)  # pausa antes de limpar
        limpar_tela()

    print(f"\n\033[31mGame Over! A palavra era: {palavra}\033[0m")  # Vermelho final

while True:
    jogar()
    resposta = input("\n\033[34mQuer jogar de novo? (s/n): \033[0m").strip().lower()
    if resposta not in ['s', 'sim']:
        print("\033[34mObrigado por jogar!\033[0m")
        break