import os

alunos = []
livros = []
emprestimo = []

def limpa_tela():
    os.system("cls")

def mostrar_livros():
    limpa_tela()
    if livros:
        print("Acervo: ")
        for i, livro in enumerate(livros):
            print( i + 1, " - ", livro["nome"], "| Situação: ", livro["situacao"])
        
    else:
        print("O acervo está vazio.")

def mostrar_alunos():
    limpa_tela()
    if alunos:
        print("Lista de Alunos: ")
        
        for i, aluno in enumerate(alunos):
            print(i + 1, " - ", aluno["nome"], "|", aluno["turma"])
        

    else:
        print("A lista de alunos está vazia")

def cadastrar_aluno():
    limpa_tela()
    nome = str(input("Digite o nome do aluno: "))
    turma = str(input("Digite a turma: "))

    novo_aluno = {
        "nome":nome,
        "turma": turma
    }
    alunos.append(novo_aluno)
    limpa_tela()
    input("Aluno cadastrado com sucesso!")
    
def cadastrar_livro():
    limpa_tela()
    nome = str(input("Digite o nome do livro: "))
    autor = str(input((f"Digite o nome do autor de {nome}: ")))
    ano = int(input(f"Digite o ano de lançamento de {nome}: "))

    novo_livro = {
        "nome":nome,
        "autor":autor,
        "ano":ano,
        "situacao": "Disponível"
    }

    livros.append(novo_livro)
    limpa_tela()
    input(f"{nome} foi cadastrado no acervo.")

def emprestimo_livro():
    limpa_tela()
    if alunos:
        mostrar_alunos()
        escolha_aluno = int(input("Digite qual aluno irá pegar o livro emprestado: "))

        if escolha_aluno > 0 and escolha_aluno <= len(alunos):
            limpa_tela()
            mostrar_livros()
            escolha_livro = int(input(f"Digite o livro que {alunos[escolha_aluno - 1]["nome"]} deseja pegar emprestado: "))
            
            if escolha_livro > 0 and escolha_livro <= len(livros) and livros[escolha_livro - 1]["situacao"] == "Disponível":
                novo_emprestimo = {
                    "titular_do_emprestimo":alunos[escolha_aluno - 1]["nome"],
                    "turma_titular":alunos[escolha_aluno - 1]["turma"],
                    "livro":livros[escolha_livro - 1]["nome"],
                    "periodo":30
                }
                emprestimo.append(novo_emprestimo)
                livros[escolha_livro - 1]["situacao"] = "Indisponível"
                limpa_tela()
                input("Empréstimo realizado.")

            else:
                limpa_tela()
                print("Opção inválida.")


        else:
            limpa_tela()
            print("Opção inválida.")        

    else:
        limpa_tela()
        input("Não há alunos cadastrados no momento.")
        return

def mostrar_emprestimos():
    limpa_tela()
    if emprestimo:
        print("Empréstimos ativos: ")
        for i, e in enumerate(emprestimo):
            print(f"{i+1} - Titular: {e["titular_do_emprestimo"]} | Turma: {e["turma_titular"]} | Livro: {e["livro"]} | Prazo: {e["periodo"]}")
    else:
        print("Não há empréstimos ativos no momento.")

def final_emprestimo():
    limpa_tela()
    if emprestimo: 
        mostrar_emprestimos()
        d = int(input("Digite qual em empréstimo será finalizado: "))

        if d > 0 and d <= len(emprestimo):
            for livro in livros:
                if livro["nome"] == emprestimo[d - 1]["livro"]:
                    livro["situacao"] = "Disponível"

            del emprestimo[d - 1]
            limpa_tela()
            print("Empréstimo finalizado.")

        else:
            limpa_tela()
            print("Opção Inválida!")

    else:
        limpa_tela()
        print("Não há empréstimo ativo no momento.")
        return

while True:
    limpa_tela()
    print("Sistema da Biblioteca\n")
    print("[1] Acervo\n[2] Lista de alunos \n[3] Cadastrar Livro\n[4] Cadastrar Aluno\n[5] Empréstimo\n[6] Sair")
    d = int(input("Escolha uma opção: "))

    if d == 1:
        mostrar_livros()
        input("Tecle enter para continuar")
        
    elif d == 2:
        mostrar_alunos()
        input("Tecle enter para continuar")

    elif d == 3:
        cadastrar_livro()

    elif d == 4:
        cadastrar_aluno()

    elif d == 5:
        limpa_tela()
        while True:
            print("[1] Pegar livro emprestado\n[2] Empréstimos Ativos\n[3] Devolução")
            d1 = int(input("Escolha uma opção: "))
            if d1 == 1:
                emprestimo_livro()
                break

            elif d1 == 2:
                mostrar_emprestimos()
                input("Tecle enter para continuar")
                break

            elif d1 == 3:
                final_emprestimo()
                input("Tecle enter para continuar")
                break

            else:
                limpa_tela()
                input("Opção inválida. Tente novamente.") 

    elif d == 6:
        print("Programa finalizado.")
        break

    elif d > 6 or d < 0:
        limpa_tela()
        input("Opção inválida. Tente novamente.")
