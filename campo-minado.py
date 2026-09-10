def mostrar_menu():
    while True:
        print("================================")
        print("          🐇 A FLORESTA")
        print("================================")
        print()
        print("Você é um pequeno coelho")
        print("perdido na floresta.")
        print()
        print("Existem várias tocas espalhadas")
        print("pelo território.")
        print()
        print("Mas os lobos estão por perto...")
        print()
        print("Encontre uma toca segura.")
        print("================================")
        print()
        print("1 - Começar jogo")
        print("2 - Como jogar")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao in ["1", "2", "3"]:
            return opcao

        print("\n⚠️ Opção inválida! Tente novamente.\n")



def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            iniciar_jogo() #diogo

        elif opcao == "2":
            mostrar_como_jogar()  # larissa

        elif opcao == "3":
            print("\nAté a próxima, coelhinho! 🐇\n")
            break



main()

def tabuleiro_facil():
    return [
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?']
    ]


def tabuleiro_medio():
    return [
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
    ]


def tabuleiro_dificil():
    return [
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
        ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
    ]

def menu_de_dificuldade():
    print(' CAMPO MINADO ')
    print(' 1) 9x9: facil ')
    print(' 2) 12x12: medio ')
    print(' 3) 12x12: dificil ')
    nivel = (input('qual o nivel você quer jogar? (1, 2 ou 3): '))

    if nivel == 1:
        return tabuleiro_facil()
    elif nivel == 2:
        return tabuleiro_medio()
    elif nivel == 3:
        return tabuleiro_dificil()
    else:
        print('o numero é invalido, selecione novamente o nivel de 1 a 3')
        return menu_de_dificuldade()


def mostrar_como_jogar():
    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║        🐇 COMO JOGAR 🐺             ║")
    print("╚══════════════════════════════════════╝")

    print("\n🌲 OBJETIVO")
    print("-" * 38)
    print("Você controla um coelhinho perdido")
    print("em uma floresta cheia de caminhos")
    print("e tocas escondidas.")
    print()
    print("Seu objetivo é encontrar todas as")
    print("tocas seguras sem encontrar um lobo!")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("\n🗺️-*-COMO FUNCIONA-*-🗺️")
    print("-" * 38)
    print("O mapa é formado por várias áreas.")
    print("Algumas escondem tocas seguras...")
    print("outras escondem lobos! 🐺")
    print()
    print("A cada rodada, escolha uma posição")
    print("do mapa para explorar.")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("\n🔎 SÍMBOLOS")
    print("-" * 38)
    print("🕳️  = Toca segura")
    print("🐺  = Lobo")
    print("❓  = Área ainda não explorada")
    print("🐇  = Você está aqui")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("\n⚠️  CUIDADO!")
    print("-" * 38)
    print("Se você encontrar um lobo,")
    print("o jogo termina! 😱")
    print()
    print("Se encontrar todas as tocas seguras,")
    print("você vence o jogo! 🎉")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("\n💡 DICA")
    print("-" * 38)
    print("Observe as áreas já exploradas")
    print("e pense bem antes de escolher")
    print("o próximo caminho!")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("\n🎮-*-EXEMPLO-*-🎮")
    print("-" * 38)
    print("Escolha uma linha e uma coluna")
    print("para explorar uma área da floresta.")
    print()
    print("Exemplo: linha 2, coluna 3")

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    input("Pressione ENTER para voltar ao menu...")
