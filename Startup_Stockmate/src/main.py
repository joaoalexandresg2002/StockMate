# main.py
# Entrada principal do StockMate — Controle de Estoque (CLI)

from typing import Optional
import models          # Importa funções e modelos de produto
import estoque         # Importa operações de manipulação do estoque
import menu            # Importa o menu da interface CLI

def ler_inteiro(prompt: str) -> int:
    while True:                         # Loop até receber entrada válida
        try:
            return int(input(prompt).strip())  # Tenta converter para inteiro
        except ValueError:
            print("Entrada inválida — digite um número inteiro.")  # Erro se não for número

def ler_texto(prompt: str, opcional: bool = False) -> str:
    while True:                         # Loop até receber texto válido
        texto = input(prompt).strip()   # Lê e remove espaços
        if texto or opcional:           # Aceita vazio apenas se for opcional
            return texto
        print("Campo obrigatório.")     # Mensagem caso esteja vazio

def ler_float_opcional(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()   # Lê valor numérico opcional
        if valor == "":
            return 0.0                  # Se vazio, retorna zero
        try:
            return float(valor.replace(",", "."))  # Aceita vírgula ou ponto
        except ValueError:
            print("Formato inválido — use números, ex: 12.50.")

def handle_adicionar():
    print("\n== Adicionar Produto ==")

    id_prod      = ler_inteiro("ID do produto: ")               # Lê ID
    nome         = ler_texto("Nome do produto: ")               # Lê nome
    quantidade   = ler_inteiro("Quantidade inicial: ")          # Lê quantidade
    preco        = ler_float_opcional("Preço unitário (ENTER para 0): ")  # Lê preço opcional

    produto = models.criar_produto(id_prod, nome, quantidade, preco)  # Cria dict do produto
    estoque.adicionar_produto(produto)                                # Adiciona ao estoque

    print(f"Produto '{nome}' adicionado com sucesso.")

def handle_remover():
    print("\n== Remover Produto ==")
    id_prod = ler_inteiro("ID do produto a remover: ")   # ID do produto

    if estoque.remover_produto(id_prod):                 # Tenta remover
        print("Produto removido.")
    else:
        print("Produto não encontrado.")

def handle_atualizar():
    print("\n== Atualizar Quantidade ==")
    id_prod   = ler_inteiro("ID do produto: ")           # ID do produto
    nova_qtde = ler_inteiro("Nova quantidade: ")         # Nova quantidade

    if estoque.atualizar_quantidade(id_prod, nova_qtde): # Atualiza se existir
        print("Quantidade atualizada.")
    else:
        print("Produto não encontrado.")

def handle_listar():
    print("\n== Lista de Produtos ==")
    produtos = estoque.listar_produtos()                # Obtém cópia da lista

    if not produtos:                                    # Se lista estiver vazia
        print("Estoque vazio.")
        return

    print(f"{'ID':<6}{'Nome':<30}{'Qtd':<8}{'Preço':<10}")  # Cabeçalhos formatados
    print("-" * 60)

    for p in produtos:                                  # Percorre lista e exibe cada produto
        print(f"{p['id']:<6}{p['nome']:<30}{p['quantidade']:<8}{p['preco']:.2f}")

def handle_buscar():
    print("\n== Buscar Produto ==")
    id_prod = ler_inteiro("ID do produto: ")            # ID do produto buscado

    p = estoque.buscar_produto(id_prod)                 # Busca no estoque
    if not p:                                           # Verifica se existe
        print("Produto não encontrado.")
        return

    print("Produto encontrado:")                        # Exibe dados do produto
    print(f"ID: {p['id']}")
    print(f"Nome: {p['nome']}")
    print(f"Quantidade: {p['quantidade']}")
    print(f"Preço: {p['preco']:.2f}")

def main():
    print("Bem-vindo ao StockMate — Sistema de Controle de Estoque")

    opcoes = {
        "1": handle_adicionar,   # Opção de adicionar
        "2": handle_remover,     # Opção de remover
        "3": handle_atualizar,   # Opção de atualizar quantidade
        "4": handle_listar,      # Opção de listar produtos
        "5": handle_buscar,      # Opção de buscar produto
    }

    while True:
        menu.exibir_menu()                       # Mostra menu
        escolha = input("Escolha uma opção: ").strip()  # Lê escolha do usuário

        if escolha == "0":                       # 0 encerra o sistema
            print("Saindo... Até mais.")
            break

        acao = opcoes.get(escolha)               # Obtém função correspondente
        if acao:
            acao()                               # Executa a ação
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  # Executa o programa principal
