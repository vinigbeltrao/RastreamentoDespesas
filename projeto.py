import os

BANCO_DE_DADOS = "planilha.csv"
def limparTela():
    os.system('cls')

limparTela()

input("\033[1;34;40mBem Vinda, \033[37mNatália\033[1;34;40m!\nDigite alguma tecla para acessar o seu sistema de catálogo de despesas pessoais. ")


def extrairPlanilha():

    transacoes = []
    with open(BANCO_DE_DADOS, "r") as planilha:
        linhas = planilha.read().split("\n")

        for linha in linhas:
            if linha:
                partes = linha.split(',')
                transacoes.append({"nome": partes[0],"categoria": partes[1],"valor": float(partes[2])})
    return transacoes

def salvarTransacao(transacoes):
    with open(BANCO_DE_DADOS, "w") as planilha:
        for transacao in transacoes:
            linha = f"{transacao['nome']},{transacao['categoria']},{transacao['valor']}"
            planilha.write(linha + '\n')

def verTransacoes(transacoes):
    if len(transacoes) == 0:
        input("No momento não existem transações, escolha a primeira opção no menu principal para adicionar uma.\nDigite algo para voltar ao menu principal.")
        menuPrincipal()
    else:
        for i, transacao in enumerate(transacoes):
            print(f"{i}. Nome: {transacao['nome']}, Categoria: {transacao['categoria']}, Valor: {transacao['valor']}")

def adicionarTransacao():
    transacoes = extrairPlanilha()

    nome = input("Digite o nome da transação: ").lower()
    categoria = input("Digite a categoria da transação: ").lower()
    valor = float(input("Digite o valor da transação: "))

    transacoes.append({"nome": nome,"categoria": categoria,"valor": valor})

    salvarTransacao(transacoes)


def deletarTransacao():
    try:
        transacoes = extrairPlanilha()

        if len(transacoes) == 0:
            input("No momento não existem transações a serem apagadas.\nDigite algo para voltar ao menu principal. ")
        else:
            verTransacoes(transacoes)

            indice_transacao = int(input('Digite o índice da transação a ser apagada: '))
            transacoes.pop(indice_transacao)

            salvarTransacao(transacoes)
    except IndexError:
        input("Índice inexistente. Pressione outra tecla para voltar ao menu. ")
        menuPrincipal()
    except ValueError:
        input("Caractér inválido.\nDigite algo para voltar ao menu principal.")
        menuPrincipal()

def totalGasto():
    totalGasto = 0
    transacoes = extrairPlanilha()
    for transacao in transacoes:
        totalGasto += transacao["valor"]
    return totalGasto

def verTransacoesPorCategorias(escolha):
    categoria = input("Informe a categoria para filtrar: ").lower()
    transacoes = extrairPlanilha()

    transacoesFiltradas = [t for t in transacoes if t["categoria"] == categoria]
    if len(transacoesFiltradas) == 0:
        input("Não existem transações com essa categoria.\nDigite algo para voltar ao menu principal.")
        menuPrincipal()

    elif escolha == "5":
        totalCategoria = 0
        total = totalGasto()
        for transacao in transacoesFiltradas:
            totalCategoria += transacao["valor"]
        porcentagemCategoria = (totalCategoria * 100) / total
        return porcentagemCategoria, categoria

    else:
        verTransacoes(transacoesFiltradas)
    

def menuPrincipal():
    try:
        while True:
            limparTela()
            print("\033[1;34;40m-" * 16 + "MENU PRINCIPAL" + "-" * 16)
            print("|" + " " * 44 + "|")
            print("| {0:42} |".format("1. Adicionar uma nova transação"))
            print("| {0:42} |".format("2. Ver transações por categoria"))
            print("| {0:42} |".format("3. Deletar uma transação"))
            print("| {0:42} |".format("4. Ver todas as transações"))
            print("| {0:42} |".format("5. Ver relação em porcentagem de gastos"))
            print("| {0:42} |".format("6. Fechar menu"))
            print("|" + " "*44 + "|")
            print("| {0:^42} |".format(f"Gasto total: R${totalGasto():.2f}"))
            print("|" + " "*44 + "|")
            print("-" * 46 + "\n")
            escolha = input("Escolha um opção: ")

            if escolha == "1":
                adicionarTransacao()
            elif escolha == "2":
                verTransacoesPorCategorias(escolha)
                input("Digite qualquer tecla para voltar para o menu principal. ")
            elif escolha == "3":
                deletarTransacao()
            elif escolha == "4":
                transacoes = extrairPlanilha()
                verTransacoes(transacoes)
                input("Digite qualquer tecla para voltar para o menu principal. ")
            elif escolha == "5":
                porcentagemCategoria, categoria = verTransacoesPorCategorias(escolha)
                print(f"Você gastou {porcentagemCategoria:.2f}% dos seus gastos com {categoria}. Se oriente!") 
                input("Digite qualquer tecla para voltar para o menu principal. ")
            elif escolha == "6":
                break
    except EOFError:
        print("Opção inválida. Tente novamente.")
        input("Digite qualquer tecla para voltar para o menu principal. ")
        menuPrincipal()
    except KeyboardInterrupt:
        print("Opção inválida. Tente novamente.")
        input("Digite qualquer tecla para voltar para o menu principal. ")
        menuPrincipal()

    except FileNotFoundError:
        with open(BANCO_DE_DADOS, "w") as planilha:
            pass

        input("Uma pasta com repósitorios econômicos foi criada. Por favor digite alguma tecla para voltar ao menu principal a fim de realizar as funções.")
        menuPrincipal()


menuPrincipal()