from cores import RESET, TITULO, OPCAO, SUCESSO, AVISO, ERRO, ITEM, DETALHE

compras = []
continuar = True

while continuar:
    print()
    print(f"{TITULO}╭──────────────────────────────╮{RESET}")
    print(f"{TITULO}│       LISTA DE COMPRAS       │{RESET}")
    print(f"{TITULO}╰──────────────────────────────╯{RESET}")
    print(f"{OPCAO}1{RESET}  Adicionar item")
    print(f"{OPCAO}2{RESET}  Ver lista")
    print(f"{OPCAO}3{RESET}  Remover item")
    print(f"{OPCAO}0{RESET}  Sair")

    escolha = input(f"\n{DETALHE}Escolha uma opção: {RESET}")

    if escolha == "1":
        item = input("Qual item deseja adicionar? ").strip()
        if item != "":
            compras.append(item)
            print(f"{SUCESSO}✓ {item} foi adicionado à lista.{RESET}")
        else:
            print(f"{AVISO}Digite o nome de um item.{RESET}")

    elif escolha == "2":
        print(f"\n{TITULO}Sua lista{RESET}")
        if len(compras) == 0:
            print(f"{DETALHE}Ainda não há itens na lista.{RESET}")
        else:
            for numero, item in enumerate(compras, start=1):
                print(f"{DETALHE}{numero:>2}.{RESET} {ITEM}{item}{RESET}")

    elif escolha == "3":
        item = input("Qual item deseja remover? ").strip()
        if item in compras:
            compras.remove(item)
            print(f"{SUCESSO}✓ {item} foi removido da lista.{RESET}")
        else:
            print(f"{ERRO}Esse item não está na lista.{RESET}")

    elif escolha == "0":
        continuar = False
        print(f"\n{SUCESSO}Lista salva nesta sessão. Até a próxima!{RESET}")

    else:
        print(f"{ERRO}Opção inválida. Escolha 1, 2, 3 ou 0.{RESET}")
