<div align="center">

# 🛒 Lista de Compras

### Um projeto simples e colorido feito em Python

Organize seus itens pelo terminal: adicione, consulte e remova produtos com um menu fácil de usar.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Projeto](https://img.shields.io/badge/Projeto-Educacional-8B5CF6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-22C55E?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

A **Lista de Compras** é um programa de terminal para praticar os fundamentos da lógica de programação com Python. Ao iniciar, o programa mostra um menu interativo para incluir produtos, conferir a lista ou remover um item.

A interface usa cores ANSI para destacar títulos, opções, confirmações e avisos. O código foi mantido simples e utiliza estruturas introdutórias, sem funções avançadas.

## ✨ Funcionalidades

- **Adicionar itens** à lista.
- **Visualizar os itens** numerados.
- **Remover um item** pelo nome.
- **Avisar** quando a lista está vazia, o item não existe ou a opção é inválida.
- **Exibir mensagens coloridas** no terminal.
- **Continuar usando o menu** até escolher a opção de sair.

## 🧠 Conceitos praticados

- Variáveis e tipos de dados básicos.
- Listas e métodos `append()` e `remove()`.
- Entrada de dados com `input()` e saída com `print()`.
- Repetição com `while`.
- Decisões com `if`, `elif` e `else`.
- Operadores de comparação e pertinência, como `==` e `in`.
- Formatação de texto com f-strings.
- Importação de variáveis de outro arquivo com `from ... import ...`.
- Códigos ANSI para colorir mensagens no terminal.

## 📁 Estrutura do projeto

```text
lista_compras/
├── main.py       # menu e funcionamento do programa
├── cores.py      # paleta de cores e estilos ANSI
└── README.md     # documentação do projeto
```

## ⚙️ Requisitos

- Python 3 instalado.
- Um terminal que aceite entrada de texto e, para exibir as cores, tenha suporte a códigos ANSI.

Não é necessário instalar bibliotecas externas.

## ▶️ Como executar

1. Baixe ou clone este projeto.
2. Abra o terminal dentro da pasta `lista_compras`.
3. Execute:

```bash
python main.py
```

Se o comando `python` não funcionar, tente:

```bash
python3 main.py
```

## 🕹️ Como usar

Quando o menu aparecer, digite o número da opção desejada e pressione **Enter**:

| Opção | Ação |
|---|---|
| `1` | Adiciona um produto. Depois, digite o nome do item. |
| `2` | Mostra os itens cadastrados, numerados. |
| `3` | Remove um item pelo nome. |
| `0` | Encerra o programa. |

### Exemplo

```text
1  Adicionar item
2  Ver lista
3  Remover item
0  Sair

Escolha uma opção: 1
Qual item deseja adicionar? café
✓ café foi adicionado à lista.
```

## 🎨 Personalização das cores

As cores e os estilos ficam separados em `cores.py`. Assim, o arquivo principal pode importar nomes fáceis de entender, como `TITULO`, `SUCESSO` e `ERRO`, em vez de repetir os códigos de cor.

Os códigos ANSI seguem o formato `\033[...m`. Por exemplo, `\033[38;5;141m` seleciona um tom de roxo e `\033[0m` encerra a formatação atual.

Para mudar uma cor, edite o valor correspondente em `cores.py`. A aparência pode variar um pouco de acordo com o terminal.

## 💾 Sobre o armazenamento

A lista existe apenas enquanto o programa está em execução. Ao escolher sair ou fechar o terminal, os itens são apagados, pois este projeto ainda não grava os dados em um arquivo.

## 🔧 Ideias para versões futuras

- Salvar e carregar a lista em um arquivo de texto.
- Permitir remover um item pelo número.
- Evitar itens duplicados.
- Adicionar uma opção para limpar a lista inteira.

## 📚 Objetivo de aprendizagem

Este projeto é uma prática introdutória: combina uma lista com um menu repetido e condições simples para resolver uma tarefa cotidiana. É possível acompanhar o fluxo do programa lendo `main.py` de cima para baixo.

---

<div align="center">
👩‍💻 Autoria
Feito por Beatris Antunes Silva durante o Bootcamp de Análise de Dados da Generation Brasil.

</div>
