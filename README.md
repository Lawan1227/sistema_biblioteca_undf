# 📚 Sistema de Biblioteca em Python

Um sistema de gerenciamento de biblioteca desenvolvido em Python para praticar os fundamentos da programação e simular operações básicas de uma biblioteca escolar.

O projeto permite cadastrar alunos e livros, controlar empréstimos e registrar a devolução de exemplares por meio de um menu interativo executado no terminal.

## 🚀 Funcionalidades

- **Cadastro de alunos:** registra o nome e a turma dos alunos.
- **Cadastro de livros:** armazena o título, o autor e o ano de lançamento.
- **Consulta ao acervo:** exibe os livros cadastrados e sua disponibilidade.
- **Lista de alunos:** apresenta os alunos registrados no sistema.
- **Empréstimo de livros:** associa um aluno a um livro e define um prazo de 30 dias.
- **Consulta de empréstimos:** exibe os empréstimos ativos, incluindo o aluno responsável, a turma, o livro e o prazo.
- **Devolução de livros:** finaliza um empréstimo e atualiza a disponibilidade do livro.

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca padrão `os`
- Estruturas de dados nativas do Python

## 📋 Conceitos de programação aplicados

Este projeto foi desenvolvido para praticar conceitos fundamentais da linguagem Python:

- Variáveis e tipos de dados.
- Listas e dicionários.
- Funções e organização do código.
- Estruturas condicionais (`if`, `elif` e `else`).
- Laços de repetição (`while` e `for`).
- Manipulação de listas com `append()` e `del`.
- Iteração com `enumerate()`.
- Entrada de dados com `input()` e exibição com `print()`.
- Validação básica de opções e controle de fluxo.

## 💻 Como executar

### 1. Instale o Python

Instale o Python 3 em seu computador, caso ainda não esteja instalado.

Site oficial: https://www.python.org/downloads/

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço do repositório no GitHub.

### 3. Entre na pasta do projeto

```bash
cd sistema-biblioteca
```

### 4. Execute o programa

```bash
python main.py
```

O nome `main.py` pressupõe que o arquivo principal tenha esse nome. Caso utilize outro nome, substitua-o no comando.

## 📖 Como utilizar

Ao iniciar o programa, um menu apresenta as seguintes opções:

| Opção | Funcionalidade |
|---|---|
| 1 | Consultar o acervo |
| 2 | Consultar a lista de alunos |
| 3 | Cadastrar um livro |
| 4 | Cadastrar um aluno |
| 5 | Acessar o menu de empréstimos |
| 6 | Encerrar o programa |

No menu de empréstimos, é possível registrar um novo empréstimo, consultar empréstimos ativos e realizar devoluções.

## ⚠️ Limitações atuais

Esta é uma versão inicial, com foco no aprendizado dos fundamentos de Python.

- Os dados ficam armazenados apenas na memória durante a execução.
- Os registros são perdidos quando o programa é encerrado.
- A validação de entradas numéricas ainda precisa ser aprimorada.
- O prazo de empréstimo é fixo em 30 dias.
- O sistema ainda não possui interface gráfica, autenticação ou banco de dados.

## 🔮 Melhorias futuras

- [ ] Salvar e carregar os dados utilizando arquivos JSON.
- [ ] Implementar persistência com SQLite.
- [ ] Validar entradas e tratar erros de digitação.
- [ ] Criar identificadores únicos para alunos, livros e empréstimos.
- [ ] Registrar datas de empréstimo e devolução.
- [ ] Calcular atrasos e datas de vencimento.
- [ ] Permitir pesquisa de livros por título e autor.
- [ ] Melhorar a organização do código em módulos.
- [ ] Desenvolver uma interface gráfica ou versão web.

## 🎯 Objetivo do projeto

Consolidar os conhecimentos iniciais de Python por meio da construção de uma aplicação prática, desenvolvendo raciocínio lógico, organização de código e capacidade de resolver problemas.

Este projeto faz parte da minha jornada de aprendizado em programação e representa uma etapa inicial na construção do meu portfólio de desenvolvimento de software.
