print("=== MENU ===")
print("1 - Olá")
print("2 - Informações")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        print("Olá! Seja bem-vindo!")
    case "2":
        print("Aqui estão as informações importantes do sistema.")
    case "3":
        print("Saindo... Até mais!")
    case _:
        print("Opção inválida! Tente novamente.")