import random

# lista das palavras
palavras = [
    'PYTHON', 'STRING', 'ALGORITIMOS', 'COMPUTADOR', 'TABELA'
]

def jogar():
    print("\033[34mJOGO DA FORCA 🕹️​\033[0m")  # Azul para o título
    print("Adivinhe a palavra!\n")

    palavra = random.choice(palavras)
    letras_descobertas = []
    letras_erradas = []
    tentativas = 6

    while tentativas > 0:
        exibicao = ''
        for letra in palavra:
            if letra in letras_descobertas:
                exibicao += f"\033[32m{letra} \033[0m"  # Verde para letras certas
            else:
                exibicao += '_ '
        print(f"\nPalavra: {exibicao.strip()}")
        print(f"\033[31mLetras erradas:\033[0m {' '.join(letras_erradas)}")  # Vermelho
        print(f"Tentativas restantes: {tentativas}")

        if all(letra in letras_descobertas for letra in palavra):
            print(f"\n\033[32mParabéns! Você acertou a palavra: {palavra}\033[0m")
            return

        tentativa = input("Digite uma letra: ").strip().upper()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("\033[33mDigite apenas UMA letra válida.\033[0m")  # Amarelo
            continue
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("\033[33mVocê já tentou essa letra.\033[0m")  # Amarelo
            continue

        if tentativa in palavra:
            print(f"\033[32mBoa! A letra '{tentativa}' está na palavra.\033[0m")  # Verde
            letras_descobertas.append(tentativa)
        else:
            print(f"\033[31mA letra '{tentativa}' não está na palavra.\033[0m")  # Vermelho
            letras_erradas.append(tentativa)
            tentativas -= 1

    print(f"\n\033[31mGame Over! A palavra era: {palavra}\033[0m")  # Vermelho final

# Início do jogo
while True:
    jogar()
    resposta = input("\nQuer jogar de novo? (s/n): ").strip().lower()
    if resposta not in ['s', 'sim']:
        print("\033[34mObrigado por jogar!\033[0m")
        break
