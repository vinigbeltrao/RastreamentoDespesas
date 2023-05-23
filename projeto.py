import os

BANCO_DE_DADOS = "planilha.csv"

def limparTela():
    os.system('cls')

def extrairPlanilha():

    transacoes = []
    with open(BANCO_DE_DADOS, 'r') as arquivo:
        linhas = arquivo.read().split('\n')

        for linha in linhas:
            if linha:
                partes = linha.split(',')
                transacoes.append({'nome': partes[0],'categoria': partes[1],'valor': float(partes[2])})
    return transacoes

def salvarTransacao(transacoes):
    with open(BANCO_DE_DADOS, 'w') as arquivo:
        for transacao in transacoes:
            linha = f"{transacao['nome']},{transacao['categoria']},{transacao['valor']}"
            arquivo.write(linha + '\n')

def verTransacoes(transacoes):
    for i, transacao in enumerate(transacoes):
        print(f"{i}. Nome: {transacao['nome']}, Categoria: {transacao['categoria']}, Valor: {transacao['valor']}")

def adicionarTransacao():
    nome = input('Digite o nome da transação: ')
    categoria = input('Digite a categoria da transação: ')
    valor = float(input('Digite o valor da transação: '))

    transacoes = extrairPlanilha()
    transacoes.append({'nome': nome,'categoria': categoria,'valor': valor})

    salvarTransacao(transacoes)


def deletarTransacao():
    transacoes = extrairPlanilha()
    verTransacoes(transacoes)

    indice_transacao = int(input('Informe o índice da transação a ser deletada: '))
    transacoes.pop(indice_transacao)

    salvarTransacao(transacoes)

def verTransacoesPorCategorias():
    categoria = input('Informe a categoria para filtrar: ')
    transacoes = extrairPlanilha()

    transacoes_filtradas = [t for t in transacoes if t['categoria'] == categoria]
    verTransacoes(transacoes_filtradas)


def menuPrincipal():
    try:
        while True:
            limparTela()
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
                verTransacoesPorCategorias()
                input("Digite qualquer tecla para voltar para o menu principal...")
            elif escolha == "3":
                deletarTransacao()
            elif escolha == "4":
                transacoes = extrairPlanilha()
                verTransacoes(transacoes)
                input("Digite qualquer tecla para voltar para o menu principal...")
            elif escolha == "5":
                break
    except EOFError:
        print("Opção inválida. Tente novamente.")
        menuPrincipal()
        input("Digite qualquer tecla para voltar para o menu principal...")
    except KeyboardInterrupt:
        print("Opção inválida. Tente novamente.")
        menuPrincipal()
        input("Digite qualquer tecla para voltar para o menu principal...")
    except FileNotFoundError:
        print("Adicione transações na planilha antes de poder ver.")
        menuPrincipal()
        input("Digite qualquer tecla para voltar para o menu principal...")

menuPrincipal()