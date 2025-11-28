import models
import estoque

def carregar_produtos_iniciais():
    produtos = [
        models.criar_produto(1, "Caderno 96 folhas", 20, 12.50),  # Cria produto com ID, nome, quantidade e preço
        models.criar_produto(2, "Caneta azul", 50, 2.00),          # Outro produto pré-definido
        models.criar_produto(3, "Borracha branca", 30, 1.50),      # Outro produto
        models.criar_produto(4, "Lápis HB", 40, 1.20),             # Outro produto
        models.criar_produto(5, "Estojo escolar", 10, 15.00),      # Outro produto
    ]

    for p in produtos:
        estoque.adicionar_produto(p)   # Adiciona cada produto ao estoque

    print("Produtos iniciais carregados com sucesso.")   # Confirma carregamento

if __name__ == "__main__":
    carregar_produtos_iniciais()       # Executa o carregamento se for chamado diretamente
    estoque.salvar_csv()               # Salva os produtos no arquivo CSV
    print("Produtos salvos em data/produtos.csv.")  # Mensagem final
