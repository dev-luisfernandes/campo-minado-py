import random


TAMANHO = 10
QUANTIDADE_LOBOS = 10
VIDAS_INICIAIS = 3

ESCONDIDO = "🌲"
TOCA = "🕳️"
LOBO = "L"
LOBO_VISIVEL = "🐺"

SIMBOLOS_TABULEIRO = {
    ESCONDIDO: "?",
    TOCA: ".",
    LOBO_VISIVEL: "L",
}


def mostrar_menu():
    print("\n================================")
    print("         🐇 A FLORESTA")
    print("================================")
    print("1 - Começar jogo")
    print("2 - Como jogar")
    print("3 - Sair")
    print("================================")

    return input("Escolha uma opção: ")


def mostrar_como_jogar():
    print("\n================================")
    print("          🐇 COMO JOGAR")
    print("================================")
    print()
    print("Você é um coelho perdido")
    print("em uma floresta cheia de lobos.")
    print()
    print(f"{SIMBOLOS_TABULEIRO[ESCONDIDO]} = Área não explorada")
    print(f"{SIMBOLOS_TABULEIRO[TOCA]} = Toca segura")
    print(f"{SIMBOLOS_TABULEIRO[LOBO_VISIVEL]} = Lobo encontrado")
    print("1-8 = Quantidade de lobos próximos")
    print()
    print("Ao encontrar uma área sem lobos")
    print("próximos, várias casas serão")
    print("abertas automaticamente.")
    print()
    print("❤️ Você possui 3 vidas.")
    print()
    print("Descubra todas as áreas seguras")
    print("antes de perder todas as vidas.")
    print()
    print("================================")

    input("\nPressione ENTER para voltar...")


def criar_floresta():
    floresta = []

    for linha in range(TAMANHO):
        nova_linha = []

        for coluna in range(TAMANHO):
            nova_linha.append(ESCONDIDO)

        floresta.append(nova_linha)

    return floresta


def criar_mapa_real():
    mapa = []

    for linha in range(TAMANHO):
        nova_linha = []

        for coluna in range(TAMANHO):
            nova_linha.append(0)

        mapa.append(nova_linha)

    return mapa


def colocar_lobos(mapa):
    lobos_colocados = 0

    while lobos_colocados < QUANTIDADE_LOBOS:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)

        if mapa[linha][coluna] != LOBO:
            mapa[linha][coluna] = LOBO
            lobos_colocados = lobos_colocados + 1


def calcular_lobos_vizinhos(mapa):
    for linha in range(TAMANHO):
        for coluna in range(TAMANHO):

            if mapa[linha][coluna] != LOBO:
                contador = 0

                for linha_vizinha in range(linha - 1, linha + 2):
                    for coluna_vizinha in range(coluna - 1, coluna + 2):

                        if linha_vizinha >= 0 and linha_vizinha < TAMANHO:
                            if coluna_vizinha >= 0 and coluna_vizinha < TAMANHO:

                                if mapa[linha_vizinha][coluna_vizinha] == LOBO:
                                    contador = contador + 1

                mapa[linha][coluna] = contador


def centralizar_texto(texto, largura):
    texto = str(texto)
    espacos = largura - len(texto)
    esquerda = espacos // 2
    direita = espacos - esquerda

    return " " * esquerda + texto + " " * direita


def mostrar_floresta(floresta):
    # Símbolos de largura fixa evitam desalinhamento dos emojis no terminal.
    largura_celula = max(2, len(str(TAMANHO))) + 2
    largura_indice = max(3, len(str(TAMANHO)))
    margem = " " * (largura_indice + 2)
    largura_grade = 1 + TAMANHO * (largura_celula + 1)
    segmento = "─" * largura_celula

    print("\n")
    print(margem + centralizar_texto("A FLORESTA", largura_grade))
    print()

    cabecalho = " ".join(
        centralizar_texto(coluna, largura_celula)
        for coluna in range(1, TAMANHO + 1)
    )
    print(margem + " " + cabecalho + " ")
    print(margem + "┌" + "┬".join([segmento] * TAMANHO) + "┐")

    for linha in range(TAMANHO):
        celulas = "│".join(
            centralizar_texto(
                SIMBOLOS_TABULEIRO.get(
                    floresta[linha][coluna], floresta[linha][coluna]
                ),
                largura_celula,
            )
            for coluna in range(TAMANHO)
        )
        print(f"{linha + 1:>{largura_indice}}  │{celulas}│")

        if linha < TAMANHO - 1:
            print(margem + "├" + "┼".join([segmento] * TAMANHO) + "┤")

    print(margem + "└" + "┴".join([segmento] * TAMANHO) + "┘")

    print()
    print(f"{margem}{SIMBOLOS_TABULEIRO[ESCONDIDO]} = Área não explorada")
    print(f"{margem}{SIMBOLOS_TABULEIRO[TOCA]} = Toca segura")
    print(f"{margem}{SIMBOLOS_TABULEIRO[LOBO_VISIVEL]} = Lobo")
    print(f"{margem}1-8 = Lobos próximos")
    print()


def abrir_area(floresta, mapa, linha, coluna):
    posicoes = []

    posicoes.append([linha, coluna])

    while len(posicoes) > 0:

        posicao = posicoes.pop(0)

        linha_atual = posicao[0]
        coluna_atual = posicao[1]

        if linha_atual >= 0 and linha_atual < TAMANHO:

            if coluna_atual >= 0 and coluna_atual < TAMANHO:

                if floresta[linha_atual][coluna_atual] == ESCONDIDO:

                    if mapa[linha_atual][coluna_atual] != LOBO:

                        valor = mapa[linha_atual][coluna_atual]

                        if valor > 0:

                            floresta[linha_atual][coluna_atual] = str(valor)

                        else:

                            floresta[linha_atual][coluna_atual] = TOCA

                            for nova_linha in range(
                                linha_atual - 1,
                                linha_atual + 2
                            ):

                                for nova_coluna in range(
                                    coluna_atual - 1,
                                    coluna_atual + 2
                                ):

                                    if nova_linha >= 0 and nova_linha < TAMANHO:

                                        if nova_coluna >= 0 and nova_coluna < TAMANHO:

                                            if mapa[nova_linha][nova_coluna] != LOBO:

                                                if floresta[nova_linha][nova_coluna] == ESCONDIDO:

                                                    posicoes.append(
                                                        [
                                                            nova_linha,
                                                            nova_coluna
                                                        ]
                                                    )


def verificar_vitoria(floresta, mapa):
    for linha in range(TAMANHO):

        for coluna in range(TAMANHO):

            if mapa[linha][coluna] != LOBO:

                if floresta[linha][coluna] == ESCONDIDO:
                    return False

    return True


def revelar_lobos(floresta, mapa):
    for linha in range(TAMANHO):

        for coluna in range(TAMANHO):

            if mapa[linha][coluna] == LOBO:
                floresta[linha][coluna] = LOBO_VISIVEL


def pedir_coordenada():
    linha_digitada = input("Digite a linha: ")
    coluna_digitada = input("Digite a coluna: ")

    if linha_digitada.isdigit() and coluna_digitada.isdigit():

        linha = int(linha_digitada)
        coluna = int(coluna_digitada)

        if (
            linha >= 1
            and linha <= TAMANHO
            and coluna >= 1
            and coluna <= TAMANHO
        ):

            linha = linha - 1
            coluna = coluna - 1

            return linha, coluna

    return -1, -1


def iniciar_jogo():
    floresta = criar_floresta()
    mapa = criar_mapa_real()

    colocar_lobos(mapa)
    calcular_lobos_vizinhos(mapa)

    vidas = VIDAS_INICIAIS
    venceu = False

    while vidas > 0 and venceu == False:

        mostrar_floresta(floresta)

        print("================================")
        print("       🐇 STATUS DO COELHO")
        print("================================")

        print("Vidas:", end=" ")

        for vida in range(vidas):
            print("❤️", end=" ")

        print()
        print("================================")
        print()

        linha, coluna = pedir_coordenada()

        if linha == -1 or coluna == -1:

            print("\n⚠️ Digite valores entre 1 e 10.")

        elif floresta[linha][coluna] != ESCONDIDO:

            print("\n⚠️ Essa posição já foi explorada!")

        elif mapa[linha][coluna] == LOBO:

            floresta[linha][coluna] = LOBO_VISIVEL
            vidas = vidas - 1

            print("\n🐺 Um lobo estava escondido aqui!")
            print("💔 Você perdeu uma vida.")

        else:

            quantidade = mapa[linha][coluna]

            if quantidade == 0:

                abrir_area(
                    floresta,
                    mapa,
                    linha,
                    coluna
                )

                print("\n🕳️ Você encontrou uma toca segura!")
                print("🌲 Parte da floresta foi revelada.")

            else:

                floresta[linha][coluna] = str(quantidade)

                print("\n✅ Área segura!")
                print("Existem", quantidade, "lobo(s) por perto.")

        venceu = verificar_vitoria(
            floresta,
            mapa
        )

    if venceu == True:

        mostrar_floresta(floresta)

        print("================================")
        print("         🏆 VOCÊ VENCEU!")
        print("================================")
        print()
        print("🐇 O coelho encontrou")
        print("todas as áreas seguras!")

    else:

        revelar_lobos(
            floresta,
            mapa
        )

        mostrar_floresta(floresta)

        print("================================")
        print("          💀 GAME OVER")
        print("================================")
        print()
        print("🐺 O coelho ficou sem vidas.")
        print("Os lobos foram revelados.")


def main():
    opcao = ""

    while opcao != "3":

        opcao = mostrar_menu()

        if opcao == "1":

            iniciar_jogo()

        elif opcao == "2":

            mostrar_como_jogar()

        elif opcao == "3":

            print()
            print("🐇 O coelho deixou a floresta...")
            print("Até a próxima!")

        else:

            print()
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()
