def menuPrincipal():
    while True:
        print("-" * 12 + "MENU PRINCIPAL" + "-" * 12)
        print("|" + " "*36 + "|")
        print("| {0:34} |".format("1. Adicionar uma nova transação"))
        print("| {0:34} |".format("2. Ver transações por categoria"))
        print("| {0:34} |".format("3. Deletar uma transação"))
        print("| {0:34} |".format("4. Ver todas as transações"))
        print("| {0:34} |".format("5. Fechar menu"))
        print("|" + " "*36 + "|")
        print("-" * 38 + "\n")
        escolha = input("Escolha um opção: ")

        if escolha == "1":
            adicionarTransacao()
        elif escolha == "2":
            verPorCategorias()
        elif escolha == "3":
            deletarTransacao()
        elif escolha == "4":
            verTransacoes()
        elif escolha == "5":
            break
menuPrincipal()