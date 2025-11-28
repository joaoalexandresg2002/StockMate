from src import estoque, models

def test_adicionar_buscar_remover():
    estoque.estoque.clear()                # Limpa o estoque global antes do teste
    produto = models.criar_produto(999, "Teste", 5, 1.0)   # Cria um produto fictício para teste

    assert estoque.adicionar_produto(produto)             # Verifica se o produto foi adicionado
    assert estoque.buscar_produto(999)["nome"] == "Teste" # Verifica se a busca retorna o produto correto
    assert estoque.remover_produto(999)                   # Verifica se o produto é removido com sucesso
